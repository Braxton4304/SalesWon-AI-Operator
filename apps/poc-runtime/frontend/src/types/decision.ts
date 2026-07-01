export type DecisionAction =
  | "answer"
  | "ask"
  | "retrieve"
  | "escalate"
  | "refuse"
  | "recommend";

export interface ChatResponse {
  response_payload: string;
  decision_action: DecisionAction;
  confidence_score: number;
  source_references: string[];
  audit_id: string;
  status?: string | null;
  pending_confirmation_id?: string | null;
  proposed_action?: Record<string, unknown> | null;
  session_id?: string | null;
  primary_agent?: string | null;
}

export interface ConfirmResponse {
  response_payload: string;
  decision_action: DecisionAction;
  confidence_score: number;
  source_references: string[];
  audit_id: string;
  status?: string | null;
}
