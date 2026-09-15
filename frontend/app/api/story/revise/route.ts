import { NextRequest, NextResponse } from 'next/server';

const BACKEND_URL = process.env.BACKEND_URL || 'http://localhost:5000';

export async function POST(request: NextRequest) {
  try {
    const { prompt, feedback } = await request.json();

    if (!prompt || !feedback) {
      return NextResponse.json(
        { error: 'Both prompt and feedback are required' },
        { status: 400 }
      );
    }

    // Call the Python backend to revise the story
    const response = await fetch(`${BACKEND_URL}/api/revise-story`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ prompt, feedback }),
    });

    if (!response.ok) {
      throw new Error('Backend API call failed');
    }

    const storyData = await response.json();

    // Evaluate the revised story
    const evaluationResponse = await fetch(`${BACKEND_URL}/api/evaluate-story`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ story: storyData.story }),
    });

    if (!evaluationResponse.ok) {
      throw new Error('Evaluation API call failed');
    }

    const evaluationData = await evaluationResponse.json();

    return NextResponse.json({
      story: storyData.story,
      evaluation: evaluationData.evaluation,
      success: true,
    });
  } catch (error) {
    console.error('Error revising story:', error);
    return NextResponse.json(
      { error: 'Failed to revise story', success: false },
      { status: 500 }
    );
  }
}
