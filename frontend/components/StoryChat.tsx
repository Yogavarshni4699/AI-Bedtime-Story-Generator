'use client';

import { useState } from 'react';
import { Message } from './Message';
import { StoryInput } from './StoryInput';
import { StoryEvaluation } from './StoryEvaluation';

interface ChatMessage {
  role: 'user' | 'assistant' | 'system';
  content: string;
  evaluation?: {
    scores: {
      simplicity: number;
      creativity: number;
      age_suitability: number;
      attractiveness: number;
      moral_value: number;
    };
    feedback: string;
  };
}

export function StoryChat() {
  const [messages, setMessages] = useState<ChatMessage[]>([
    {
      role: 'assistant',
      content: "Hello! I'm your AI storyteller. What kind of bedtime story would you like to hear tonight? Tell me about your favorite animals, adventures, or magical places!",
    },
  ]);
  const [isLoading, setIsLoading] = useState(false);
  const [currentStoryPrompt, setCurrentStoryPrompt] = useState<string>('');

  const generateStory = async (prompt: string) => {
    setIsLoading(true);
    setCurrentStoryPrompt(prompt);

    // Add user message
    setMessages((prev) => [...prev, { role: 'user', content: prompt }]);

    try {
      const response = await fetch('/api/story', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ prompt }),
      });

      if (!response.ok) {
        throw new Error('Failed to generate story');
      }

      const data = await response.json();

      // Add assistant message with story and evaluation
      setMessages((prev) => [
        ...prev,
        {
          role: 'assistant',
          content: data.story,
          evaluation: data.evaluation,
        },
      ]);
    } catch (error) {
      setMessages((prev) => [
        ...prev,
        {
          role: 'system',
          content: 'Sorry, I had trouble creating a story. Please try again!',
        },
      ]);
    } finally {
      setIsLoading(false);
    }
  };

  const reviseStory = async (feedback: string) => {
    if (!currentStoryPrompt) return;

    setIsLoading(true);

    // Add user feedback message
    setMessages((prev) => [...prev, { role: 'user', content: `Please revise: ${feedback}` }]);

    try {
      const response = await fetch('/api/story/revise', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ prompt: currentStoryPrompt, feedback }),
      });

      if (!response.ok) {
        throw new Error('Failed to revise story');
      }

      const data = await response.json();

      // Add revised story
      setMessages((prev) => [
        ...prev,
        {
          role: 'assistant',
          content: data.story,
          evaluation: data.evaluation,
        },
      ]);
    } catch (error) {
      setMessages((prev) => [
        ...prev,
        {
          role: 'system',
          content: 'Sorry, I had trouble revising the story. Please try again!',
        },
      ]);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="bg-white rounded-2xl shadow-2xl overflow-hidden">
      {/* Chat Messages Area */}
      <div className="h-[500px] overflow-y-auto p-6 space-y-4">
        {messages.map((msg, idx) => (
          <div key={idx}>
            <Message message={msg} />
            {msg.evaluation && (
              <StoryEvaluation
                evaluation={msg.evaluation}
                onRevise={reviseStory}
                isLoading={isLoading}
              />
            )}
          </div>
        ))}
        {isLoading && (
          <div className="flex items-center space-x-2 text-gray-500">
            <div className="animate-spin rounded-full h-4 w-4 border-b-2 border-indigo-600"></div>
            <span>Creating your story...</span>
          </div>
        )}
      </div>

      {/* Input Area */}
      <StoryInput onSubmit={generateStory} isLoading={isLoading} />
    </div>
  );
}
