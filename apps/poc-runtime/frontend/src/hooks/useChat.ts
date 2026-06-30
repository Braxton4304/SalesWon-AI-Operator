import { useCallback, useState } from "react";
import { confirmAction, sendChat } from "../api/chatClient";
import type { ChatMessage } from "../types/message";

function newId() {
  return crypto.randomUUID();
}

export function useChat(userId: string, sessionId: string | null, onSessionId: (id: string) => void) {
  const [messages, setMessages] = useState<ChatMessage[]>([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const appendAssistant = useCallback((payload: {
    content: string;
    decision_action?: ChatMessage["decision_action"];
    confidence_score?: number;
    status?: string | null;
    pending_confirmation_id?: string | null;
    proposed_action?: Record<string, unknown> | null;
  }) => {
    setMessages((prev) => [
      ...prev,
      {
        id: newId(),
        role: "assistant",
        ...payload,
      },
    ]);
  }, []);

  const sendMessage = useCallback(
    async (text: string) => {
      setError(null);
      setLoading(true);
      setMessages((prev) => [...prev, { id: newId(), role: "user", content: text }]);
      try {
        const result = await sendChat(text, userId, sessionId);
        if (result.session_id) onSessionId(result.session_id);
        appendAssistant({
          content: result.response_payload,
          decision_action: result.decision_action,
          confidence_score: result.confidence_score,
          status: result.status,
          pending_confirmation_id: result.pending_confirmation_id,
          proposed_action: result.proposed_action ?? undefined,
        });
      } catch (err) {
        setError(err instanceof Error ? err.message : "Unknown error");
      } finally {
        setLoading(false);
      }
    },
    [appendAssistant, onSessionId, sessionId, userId]
  );

  const confirmPending = useCallback(
    async (pendingId: string) => {
      setError(null);
      setLoading(true);
      try {
        const result = await confirmAction(pendingId, userId, sessionId);
        appendAssistant({
          content: result.response_payload,
          decision_action: result.decision_action,
          confidence_score: result.confidence_score,
          status: result.status,
        });
      } catch (err) {
        setError(err instanceof Error ? err.message : "Unknown error");
      } finally {
        setLoading(false);
      }
    },
    [appendAssistant, sessionId, userId]
  );

  const clearMessages = useCallback(() => setMessages([]), []);

  return { messages, loading, error, sendMessage, confirmPending, clearMessages };
}
