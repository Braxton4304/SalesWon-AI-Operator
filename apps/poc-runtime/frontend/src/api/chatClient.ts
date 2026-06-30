import type { ChatResponse, ConfirmResponse } from "../types/decision";

const API_BASE = "";

function headers(userId: string): HeadersInit {
  return {
    "Content-Type": "application/json",
    "X-User-Id": userId,
  };
}

export async function sendChat(
  message: string,
  userId: string,
  sessionId?: string | null
): Promise<ChatResponse> {
  const response = await fetch(`${API_BASE}/chat`, {
    method: "POST",
    headers: headers(userId),
    body: JSON.stringify({ message, session_id: sessionId }),
  });
  if (!response.ok) {
    const detail = await response.text();
    throw new Error(detail || "Chat request failed");
  }
  return response.json();
}

export async function confirmAction(
  pendingConfirmationId: string,
  userId: string,
  sessionId?: string | null
): Promise<ConfirmResponse> {
  const response = await fetch(`${API_BASE}/chat/confirm`, {
    method: "POST",
    headers: headers(userId),
    body: JSON.stringify({
      pending_confirmation_id: pendingConfirmationId,
      session_id: sessionId,
    }),
  });
  if (!response.ok) {
    const detail = await response.text();
    throw new Error(detail || "Confirm request failed");
  }
  return response.json();
}

export async function checkHealth(): Promise<boolean> {
  const response = await fetch(`${API_BASE}/health`);
  return response.ok;
}
