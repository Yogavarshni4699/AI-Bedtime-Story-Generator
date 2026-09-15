interface MessageProps {
  message: {
    role: 'user' | 'assistant' | 'system';
    content: string;
  };
}

export function Message({ message }: MessageProps) {
  const isUser = message.role === 'user';
  const isSystem = message.role === 'system';

  return (
    <div className={`flex ${isUser ? 'justify-end' : 'justify-start'}`}>
      <div
        className={`max-w-[80%] rounded-2xl px-4 py-3 ${
          isUser
            ? 'bg-indigo-600 text-white'
            : isSystem
            ? 'bg-red-100 text-red-800 border border-red-300'
            : 'bg-gray-100 text-gray-900'
        }`}
      >
        {!isUser && !isSystem && (
          <div className="text-xs font-semibold text-indigo-600 mb-1">
            Story Assistant
          </div>
        )}
        <div className="whitespace-pre-wrap">{message.content}</div>
      </div>
    </div>
  );
}
