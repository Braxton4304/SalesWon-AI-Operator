import { AppShell } from "./components/Layout/AppShell";
import { ChatWindow } from "./components/Chat/ChatWindow";
import { useChat } from "./hooks/useChat";
import { useSession } from "./hooks/useSession";

export default function App() {
  const { userId, setUserId, sessionId, updateSessionId, resetSession } = useSession();
  const { messages, loading, error, sendMessage, confirmPending, clearMessages } = useChat(
    userId,
    sessionId,
    updateSessionId
  );

  const handleReset = () => {
    resetSession();
    clearMessages();
  };

  return (
    <AppShell userId={userId} onUserIdChange={setUserId} onResetSession={handleReset}>
      <ChatWindow
        messages={messages}
        loading={loading}
        error={error}
        onSend={sendMessage}
        onConfirm={confirmPending}
      />
    </AppShell>
  );
}
