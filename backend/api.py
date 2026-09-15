from flask import Flask, request, jsonify
from flask_cors import CORS
from agents import storyteller_agent, judge_agent
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend communication


@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({"status": "healthy", "message": "AI Bedtime Story Generator API is running"})


@app.route('/api/generate-story', methods=['POST'])
def generate_story():
    """
    Generates a bedtime story based on user prompt.
    Expects JSON: {"prompt": "story request"}
    Returns: {"story": "generated story", "category": "extracted category"}
    """
    try:
        data = request.get_json()
        user_prompt = data.get('prompt', '')

        if not user_prompt:
            return jsonify({"error": "Prompt is required"}), 400

        # Generate initial story
        story = storyteller_agent(user_prompt)

        return jsonify({
            "story": story,
            "success": True
        })

    except Exception as e:
        print(f"Error generating story: {str(e)}")
        import traceback
        traceback.print_exc()
        return jsonify({"error": str(e), "success": False}), 500


@app.route('/api/evaluate-story', methods=['POST'])
def evaluate_story():
    """
    Evaluates a story using the judge agent.
    Expects JSON: {"story": "story text"}
    Returns: {"scores": {...}, "feedback": "..."}
    """
    try:
        data = request.get_json()
        story = data.get('story', '')

        if not story:
            return jsonify({"error": "Story is required"}), 400

        # Evaluate story
        evaluation = judge_agent(story)

        return jsonify({
            "evaluation": evaluation,
            "success": True
        })

    except Exception as e:
        return jsonify({"error": str(e), "success": False}), 500


@app.route('/api/revise-story', methods=['POST'])
def revise_story():
    """
    Revises a story based on feedback.
    Expects JSON: {"prompt": "original request", "feedback": "feedback text"}
    Returns: {"story": "revised story"}
    """
    try:
        data = request.get_json()
        user_prompt = data.get('prompt', '')
        feedback = data.get('feedback', '')

        if not user_prompt or not feedback:
            return jsonify({"error": "Both prompt and feedback are required"}), 400

        # Revise story with feedback
        revised_story = storyteller_agent(user_prompt, feedback=feedback)

        return jsonify({
            "story": revised_story,
            "success": True
        })

    except Exception as e:
        return jsonify({"error": str(e), "success": False}), 500


@app.route('/api/story-workflow', methods=['POST'])
def story_workflow():
    """
    Complete story workflow: Generate → Judge → Revise → Final evaluation
    Expects JSON: {"prompt": "story request", "userFeedback": "optional feedback"}
    Returns complete workflow data
    """
    try:
        data = request.get_json()
        user_prompt = data.get('prompt', '')
        user_feedback = data.get('userFeedback', '')

        if not user_prompt:
            return jsonify({"error": "Prompt is required"}), 400

        # Step 1: Generate initial story
        initial_story = storyteller_agent(user_prompt)

        # Step 2: Judge evaluates the story
        evaluation = judge_agent(initial_story)
        judge_feedback = evaluation.get("feedback", "")

        # Step 3: Revise based on judge feedback
        revised_story = storyteller_agent(user_prompt, feedback=judge_feedback)

        # Step 4: If user provides feedback, revise again
        final_story = revised_story
        final_evaluation = None

        if user_feedback.strip():
            final_story = storyteller_agent(user_prompt, feedback=user_feedback)
            final_evaluation = judge_agent(final_story)

        return jsonify({
            "initialStory": initial_story,
            "initialEvaluation": evaluation,
            "revisedStory": revised_story,
            "finalStory": final_story,
            "finalEvaluation": final_evaluation,
            "success": True
        })

    except Exception as e:
        return jsonify({"error": str(e), "success": False}), 500


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
