import { MessageInput } from "../MessageInput";
import { MessageList } from "../MessageList";
import "./ChatWindow.css";

interface Props {
  messages: ReturnType<typeof import("../../../hooks/useChat").useChat>["messages"];
  loading: boolean;
  error: string | null;
  onSend: (message: string) => void;
  onConfirm: (pendingId: string) => void;
}

export function ChatWindow({ messages, loading, error, onSend, onConfirm }: Props) {
  return (
    <div className="chat-window">
      <MessageList messages={messages} onConfirm={onConfirm} loading={loading} />
      {error && <div className="chat-error">{error}</div>}
      <MessageInput onSend={onSend} disabled={loading} />
    </div>
  );
}
