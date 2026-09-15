'use client';

import { useState } from 'react';

interface StoryEvaluationProps {
  evaluation: {
    scores: {
      simplicity: number;
      creativity: number;
      age_suitability: number;
      attractiveness: number;
      moral_value: number;
    };
    feedback: string;
  };
  onRevise: (feedback: string) => void;
  isLoading: boolean;
}

export function StoryEvaluation({ evaluation, onRevise, isLoading }: StoryEvaluationProps) {
  const [showRevision, setShowRevision] = useState(false);
  const [revisionInput, setRevisionInput] = useState('');

  const scores = evaluation.scores;
  const avgScore =
    Object.values(scores).reduce((a, b) => a + b, 0) / Object.values(scores).length;

  const handleRevise = () => {
    if (revisionInput.trim()) {
      onRevise(revisionInput.trim());
      setRevisionInput('');
      setShowRevision(false);
    }
  };

  return (
    <div className="mt-3 ml-12 p-4 bg-indigo-50 rounded-lg border border-indigo-200">
      <div className="text-sm font-semibold text-indigo-900 mb-2">
        Story Evaluation (Avg: {avgScore.toFixed(1)}/10)
      </div>

      <div className="grid grid-cols-2 md:grid-cols-3 gap-2 mb-3">
        {Object.entries(scores).map(([key, value]) => (
          <div key={key} className="text-xs">
            <span className="capitalize text-gray-700">
              {key.replace('_', ' ')}:
            </span>{' '}
            <span className="font-semibold text-indigo-700">{value}/10</span>
          </div>
        ))}
      </div>

      <div className="text-sm text-gray-700 mb-3 italic">
        "{evaluation.feedback}"
      </div>

      {!showRevision ? (
        <button
          onClick={() => setShowRevision(true)}
          className="text-xs px-3 py-1 bg-white border border-indigo-300 text-indigo-700 rounded-full hover:bg-indigo-50 transition-colors"
        >
          Suggest Changes
        </button>
      ) : (
        <div className="flex space-x-2">
          <input
            type="text"
            value={revisionInput}
            onChange={(e) => setRevisionInput(e.target.value)}
            placeholder="What would you like to change?"
            className="flex-1 px-3 py-1 text-sm border border-indigo-300 rounded-full focus:outline-none focus:ring-2 focus:ring-indigo-500"
            disabled={isLoading}
          />
          <button
            onClick={handleRevise}
            disabled={!revisionInput.trim() || isLoading}
            className="px-3 py-1 text-sm bg-indigo-600 text-white rounded-full hover:bg-indigo-700 disabled:bg-gray-400 transition-colors"
          >
            Revise
          </button>
          <button
            onClick={() => setShowRevision(false)}
            className="px-3 py-1 text-sm bg-gray-200 text-gray-700 rounded-full hover:bg-gray-300 transition-colors"
          >
            Cancel
          </button>
        </div>
      )}
    </div>
  );
}
