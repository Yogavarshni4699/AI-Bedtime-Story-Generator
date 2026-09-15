'use client';

import { useState } from 'react';
import { StoryChat } from '@/components/StoryChat';

export default function Home() {
  return (
    <div className="min-h-screen bg-gradient-to-b from-indigo-100 via-purple-50 to-pink-100">
      <div className="container mx-auto px-4 py-8 max-w-4xl">
        <header className="text-center mb-8">
          <h1 className="text-4xl md:text-5xl font-bold text-indigo-900 mb-2">
            🌙 AI Bedtime Story Generator
          </h1>
          <p className="text-lg text-gray-700">
            Tell me what kind of story you'd like, and I'll create a magical bedtime tale just for you!
          </p>
        </header>

        <StoryChat />

        <footer className="mt-12 text-center text-sm text-gray-600">
          <p>Stories crafted with love for children aged 5-10 ✨</p>
        </footer>
      </div>
    </div>
  );
}
