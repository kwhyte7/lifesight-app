export interface Message {
  id: string;
  content: string;
  sender: 'user' | 'ai';
  timestamp: string;
}

const API_BASE_URL = 'http://localhost:8000/api'; // Backend base URL

/**
 * Send a message to the AI and get a response
 */
export async function sendMessage(content: string): Promise<Message> {
  const response = await fetch(`${API_BASE_URL}/chat`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ message: content }),
  });

  if (!response.ok) {
    throw new Error(`API request failed: ${response.statusText}`);
  }

  const data = await response.json();

  return {
    id: data.id || Date.now().toString(),
    content: data.reply,
    sender: 'ai',
    timestamp: new Date().toISOString(),
  };
}

/**
 * Get chat history (if implemented in backend)
 */
export async function getChatHistory(): Promise<Message[]> {
  const response = await fetch(`${API_BASE_URL}/chat/history`);

  if (!response.ok) {
    throw new Error(`API request failed: ${response.statusText}`);
  }

  const data = await response.json();
  return data.messages;
}

/**
 * Clear chat history (if implemented in backend)
 */
export async function clearChatHistory(): Promise<void> {
  const response = await fetch(`${API_BASE_URL}/chat/history`, {
    method: 'DELETE',
  });

  if (!response.ok) {
    throw new Error(`API request failed: ${response.statusText}`);
  }
}
