import type { ChatMessage } from "../../../types/message";
import "./DecisionBadge.css";

interface Props {
  action?: ChatMessage["decision_action"];
  confidence?: number;
  status?: string | null;
  primaryAgent?: string | null;
}

export function DecisionBadge({ action, confidence, status, primaryAgent }: Props) {
  if (!action) return null;
  return (
    <div className="decision-badge">
      <span className={`badge badge-${action}`}>{action}</span>
      {primaryAgent && <span className="agent-tag">{primaryAgent}</span>}
      {confidence !== undefined && (
        <span className="confidence">{(confidence * 100).toFixed(0)}%</span>
      )}
      {status && <span className="status">{status}</span>}
    </div>
  );
}
