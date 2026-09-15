# AI Bedtime Story Generator - Backend

This is the Python backend API for the AI Bedtime Story Generator.

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Create a `.env` file with your OpenAI API key:
```
OPENAI_API_KEY=your_key_here
PORT=5000
```

3. Run the API server:
```bash
python api.py
```

## API Endpoints

### `POST /api/generate-story`
Generate a new bedtime story.
```json
{
  "prompt": "A story about a brave little mouse"
}
```

### `POST /api/evaluate-story`
Evaluate a story using the judge agent.
```json
{
  "story": "Once upon a time..."
}
```

### `POST /api/revise-story`
Revise a story based on feedback.
```json
{
  "prompt": "Original story request",
  "feedback": "Make it funnier"
}
```

### `POST /api/story-workflow`
Complete workflow with automatic judge feedback and optional user feedback.
```json
{
  "prompt": "A story about friendship",
  "userFeedback": "Add more animals"
}
```

## Running the CLI Version

To run the original CLI version:
```bash
python main.py
```
