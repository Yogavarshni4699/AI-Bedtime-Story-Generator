# 🌙 AI Bedtime Story Generator

An intelligent storytelling application that generates, evaluates, and refines bedtime stories for children aged 5-10 using AI agents.

<img width="1602" height="940" alt="image" src="https://github.com/user-attachments/assets/342456d3-42f3-4171-9690-1221571fa25e" />


## given :
## Instructions
The attached code is a simple python script skeleton. Your goal is to take any simple bedtime story request and use prompting to tell a story appropriate for ages 5 to 10.
- Incorporate a LLM judge to improve the quality of the story
- Provide a block diagram of the system you create that illustrates the flow of the prompts and the interaction between judge, storyteller, user, and any other components you add
- Do not change the openAI model that is being used. 
- Please use your own openAI key, but do not include it in your final submission.
- Otherwise, you may change any code you like or add any files

---

## Rules
- This assignment is open-ended
- You may use any resources you like with the following restrictions
   - They must be resources that would be available to you if you worked here (so no other humans, no closed AIs, no unlicensed code, etc.)
   - Allowed resources include but not limited to Stack overflow, random blogs, chatGPT et al
   - You have to be able to explain how the code works, even if chatGPT wrote it
- DO NOT PUSH THE API KEY TO GITHUB. OpenAI will automatically delete it

---

## What does "tell a story" mean?
It should be appropriate for ages 5-10. Other than that it's up to you. Here are some ideas to help get the brain-juices flowing!
- Use story arcs to tell better stories
- Allow the user to provide feedback or request changes
- Categorize the request and use a tailored generation strategy for each category

---

## How will I be evaluated
Good question. We want to know the following:
- The efficacy of the system you design to create a good story
- Are you comfortable using and writing a python script
- What kinds of prompting strategies and agent design strategies do you use
- Are the stories your tool creates good?
- Can you understand and deconstruct a problem
- Can you operate in an open-ended environment
- Can you surprise us

---

## Other FAQs
- How long should I spend on this? 
No more than 2-3 hours
- Can I change what the input is? 
Sure
- How long should the story be?
You decide


# My info:

## 🎯 How It Works

1. **User Prompt** → Storyteller generates Story V1
2. **Judge** evaluates → Provides feedback + metrics + decision
3. **Storyteller** → Creates Story V2 (auto-refined)
4. **Show to User** → Display revised story
5. **(Optional) User Feedback** → User suggests changes
6. **Storyteller** → Creates Story V3 (user-revised)
7. **Judge** → Final re-evaluation
8. **Final Story** → Delivered!

## 📊 Judge Evaluation Metrics

Stories are evaluated on 5 binary metrics:
- ✅ **Age Suitability**: Simple words, gentle tone
- ✅ **Relevance to Prompt**: Matches user request
- ✅ **Moral Coherence**: Clear, positive moral lesson
- ✅ **Creativity**: Imaginative and engaging
- ✅ **Safety**: No inappropriate content

**Decision**: ✅ Approved (all pass) or ⚠️ Needs revision (any fail)


## ✨ Features

- **AI Storyteller Agent**: Creates engaging, age-appropriate bedtime stories
- **AI Judge Agent**: Evaluates stories on multiple metrics with specific improvement suggestions
- **Automatic Refinement**: Stories are automatically improved based on judge feedback
- **User Feedback Loop**: Users can provide additional feedback for further revisions
- **Multi-Agent System**: Storyteller and Judge agents work together to create perfect stories

## 🏗️ Architecture

### Backend (Python/Flask)
- **Storyteller Agent**: Generates stories with controllable quality modes (good/flawed/not_kid)
- **Judge Agent**: Evaluates stories on:
  - Age suitability
  - Relevance to prompt
  - Moral coherence
  - Creativity
  - Safety
- **RESTful API**: Endpoints for story generation, evaluation, and revision

### Frontend (Next.js/React)
- **Interactive Chat Interface**: User-friendly conversation-style interaction
- **Real-time Feedback**: Shows judge evaluations and metrics
- **Workflow Visualization**: Displays the complete story refinement process
- **Responsive Design**: Works on all devices

## 🚀 Quick Deploy

### Deploy to Render (One-Click)
📖 **Detailed instructions:** See [DEPLOYMENT.md](DEPLOYMENT.md)

### Backend Setup
```bash
cd backend
pip install -r requirements.txt
cp .env.example .env
# Add your OPENAI_API_KEY to .env
python api.py
```
Backend runs on: http://localhost:5001

### Frontend Setup
```bash
cd frontend
npm install
cp .env.example .env
# Set BACKEND_URL=http://localhost:5001 in .env
npm run dev
```
Frontend runs on: http://localhost:3000

## 📋 API Endpoints

### Backend API

- `GET /api/health` - Health check
- `POST /api/generate-story` - Generate a story
- `POST /api/evaluate-story` - Evaluate a story
- `POST /api/revise-story` - Revise story with feedback
- `POST /api/story-workflow` - Complete workflow (generate → judge → revise)

### Example Request
```bash
curl -X POST http://localhost:5001/api/story-workflow \
  -H "Content-Type: application/json" \
  -d '{"prompt": "A friendly rabbit who learns to share"}'
```

## 🔧 Configuration

### Environment Variables

**Backend (.env):**
```env
OPENAI_API_KEY=your_api_key_here
PORT=5001
```

**Frontend (.env.local):**
```env
BACKEND_URL=http://localhost:5001
```

## 📁 Project Structure

```
.
├── backend/
│   ├── api.py              # Flask API server
│   ├── agents.py           # Storyteller & Judge agents
│   ├── utils.py            # OpenAI API wrapper
│   ├── main_cli.py         # CLI version
│   └── requirements.txt    # Python dependencies
├── frontend/
│   ├── app/                # Next.js pages
│   ├── components/         # React components
│   └── package.json        # Node dependencies
├── render.yaml             # Render deployment config
├── .github/
│   └── workflows/
│       └── deploy.yml      # GitHub Actions CI/CD
└── DEPLOYMENT.md           # Detailed deployment guide
```

## 🤖 GitHub Actions

Automatic deployment on every push to `main`:
1. Add `RENDER_API_KEY` to GitHub Secrets
2. Add `RENDER_SERVICE_ID` to GitHub Secrets
3. Push to main → Auto-deploy!

## 🧪 Testing

Test the judge with different prompts:
- **Good Story**: "A friendly rabbit who learns to share toys with friends"
- **Creative**: "A magical dragon who becomes friends with a brave little girl"
- **Vague** (may fail): "Tell me something nice"
- **Too Complex** (may fail): "A philosophical exploration of quantum mechanics"

## 🙏 Acknowledgments

- Built with OpenAI GPT-3.5-turbo
- Powered by Flask and Next.js
- Deployed on Render
---

**Made with ❤️ for children aged 5-10** ✨
