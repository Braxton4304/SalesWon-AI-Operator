import { useCallback, useState } from "react";

const USER_KEY = "saleswon_dev_user_id";
const SESSION_KEY = "saleswon_session_id";

export function useSession() {
  const [userId, setUserIdState] = useState(
    () => localStorage.getItem(USER_KEY) || "alice"
  );
  const [sessionId, setSessionId] = useState<string | null>(
    () => localStorage.getItem(SESSION_KEY)
  );

  const setUserId = useCallback((value: string) => {
    setUserIdState(value);
    localStorage.setItem(USER_KEY, value);
  }, []);

  const updateSessionId = useCallback((value: string | null | undefined) => {
    if (value) {
      setSessionId(value);
      localStorage.setItem(SESSION_KEY, value);
    }
  }, []);

  const resetSession = useCallback(() => {
    setSessionId(null);
    localStorage.removeItem(SESSION_KEY);
  }, []);

  return { userId, setUserId, sessionId, updateSessionId, resetSession };
}
