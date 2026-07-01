import type { ChatResponse, ConfirmResponse } from "./decision";

export type MessageRole = "user" | "assistant";

export interface ChatMessage {
  id: string;
  role: MessageRole;
  content: string;
  decision_action?: ChatResponse["decision_action"];
  confidence_score?: number;
  status?: string | null;
  pending_confirmation_id?: string | null;
  proposed_action?: Record<string, unknown> | null;
  primary_agent?: string | null;
}

export type { ChatResponse, ConfirmResponse };
