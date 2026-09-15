# AI Bedtime Story Generator - Frontend

This is the Next.js frontend chatbot interface for the AI Bedtime Story Generator.

## Features

- Interactive chat interface for story requests
- Real-time story generation with automatic evaluation
- Story revision based on user feedback
- Beautiful UI with Tailwind CSS
- Responsive design for all devices

## Setup

1. Install dependencies:
```bash
npm install
```

2. Create a `.env.local` file:
```
BACKEND_URL=http://localhost:5000
```

3. Run the development server:
```bash
npm run dev
```

4. Open [http://localhost:3000](http://localhost:3000) in your browser.

## Building for Production

```bash
npm run build
npm start
```

## Tech Stack

- Next.js 15 (App Router)
- TypeScript
- Tailwind CSS
- Vercel AI SDK
- React Hooks

## API Integration

The frontend communicates with the Python backend via REST API:

- `POST /api/story` - Generate a new story
- `POST /api/story/revise` - Revise story based on feedback

These Next.js API routes proxy requests to the Python backend at `http://localhost:5000`.

---

This is a [Next.js](https://nextjs.org) project bootstrapped with [`create-next-app`](https://nextjs.org/docs/app/api-reference/cli/create-next-app).
