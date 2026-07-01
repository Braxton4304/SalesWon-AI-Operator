import type { ChatMessage } from "../../../types/message";
import { ClarificationPrompt } from "../ClarificationPrompt";
import { ConfirmationDialog } from "../ConfirmationDialog";
import { DecisionBadge } from "../DecisionBadge";
import "./MessageList.css";

interface Props {
  messages: ChatMessage[];
  onConfirm: (pendingId: string) => void;
  loading?: boolean;
}

export function MessageList({ messages, onConfirm, loading }: Props) {
  return (
    <div className="message-list">
      {messages.map((msg) => (
        <div key={msg.id} className={`message message-${msg.role}`}>
          <div className="message-role">{msg.role === "user" ? "You" : "SalesWon AI"}</div>
          <div className="message-content">{msg.content}</div>
          {msg.role === "assistant" && (
            <>
              <DecisionBadge
                action={msg.decision_action}
                confidence={msg.confidence_score}
                status={msg.status}
                primaryAgent={msg.primary_agent}
              />
              {msg.decision_action === "ask" && (
                <ClarificationPrompt content={msg.content} />
              )}
              {msg.decision_action === "recommend" && (
                <ConfirmationDialog
                  proposedAction={msg.proposed_action}
                  pendingId={msg.pending_confirmation_id}
                  onConfirm={onConfirm}
                  loading={loading}
                />
              )}
            </>
          )}
        </div>
      ))}
    </div>
  );
}
