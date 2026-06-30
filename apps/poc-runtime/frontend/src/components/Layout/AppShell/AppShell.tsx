import { ReactNode } from "react";
import "./AppShell.css";

interface Props {
  userId: string;
  onUserIdChange: (value: string) => void;
  onResetSession: () => void;
  children: ReactNode;
}

export function AppShell({ userId, onUserIdChange, onResetSession, children }: Props) {
  return (
    <div className="app-shell">
      <header className="app-header">
        <div>
          <h1>SalesWon AI</h1>
          <p className="subtitle">POC Runtime v1 — Connector-Ready</p>
        </div>
        <div className="dev-controls">
          <label>
            Dev User ID
            <input
              type="text"
              value={userId}
              onChange={(e) => onUserIdChange(e.target.value)}
              placeholder="X-User-Id"
            />
          </label>
          <button type="button" onClick={onResetSession}>
            New session
          </button>
        </div>
      </header>
      <main className="app-main">{children}</main>
    </div>
  );
}
