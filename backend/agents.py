import json
from utils import call_model


def storyteller_agent(user_prompt, feedback=None):
    """
    Generates or revises a children's story based on the user prompt
    and optional feedback from the judge or user.

    Args:
        user_prompt: The user's story request
        feedback: Optional feedback for story revision

    Returns:
        Generated or revised story as a string
    """

    if feedback:
        # Used when revising story based on judge or user feedback
        prompt = f"""
        Revise this story based on the feedback below.
        STORY REQUEST: "{user_prompt}"
        FEEDBACK: {feedback}
        Keep it fun, simple, and engaging for kids aged 5–10.
        Use easy English, add a clear beginning, middle, and end,
        and end with a positive moral or lesson.
        """
    else:
        # First-time story generation
        prompt = f"""
        You are a kind storyteller who writes bedtime stories for children aged 5–10.

        First, think step-by-step:
        1. Identify what kind of story this is (e.g., animal, fantasy, moral, adventure, or sci-fi).
        2. Plan the beginning, middle, and end.
        3. Then write the full story in that style.

        At the top of your story, include a line like "Category: Fantasy" before starting.

        The user's request is: "{user_prompt}"

        Write a story that:
        - Uses short, clear, and simple sentences
        - Has a beginning, middle, and end
        - Includes creativity and imagination
        - Avoids harsh or negative words
        - Ends with a positive moral or life lesson
        - Is under 400 words
        """

    # Generate story using OpenAI model and 0.8 for creativity
    story = call_model(prompt, temperature=0.8)
    return story.strip()


def judge_agent(story):
    """
    Evaluates the story and provides structured feedback.
    Returns a JSON-like response with scores and feedback text.

    Args:
        story: The story to evaluate

    Returns:
        Dictionary containing scores and feedback
    """

    prompt = f"""
    You are a children's story critic for ages 5–10.
    Evaluate the story below on these criteria (1–10 scale):
    1. Simplicity of language
    2. Creativity and imagination
    3. Age appropriateness
    4. Attractiveness for kids
    5. Moral or lesson clarity

    STORY:
    {story}

    Please respond strictly in JSON format like this:
    {{
      "scores": {{
        "simplicity": 8,
        "creativity": 9,
        "age_suitability": 10,
        "attractiveness": 9,
        "moral_value": 10
      }},
      "feedback": "Short 2–3 line comment with any context-appropriate ideas for improvement."
    }}
    """

    result = call_model(prompt, temperature=0.3)

    # Try parsing JSON
    try:
        evaluation = json.loads(result)
    except json.JSONDecodeError:
        evaluation = {"scores": {}, "feedback": result.strip()}

    # Calculate average score (if numeric scores exist)
    scores = evaluation.get("scores", {})
    if scores:
        numeric_scores = [v for v in scores.values() if isinstance(v, (int, float))]
        if numeric_scores:
            avg_score = sum(numeric_scores) / len(numeric_scores)

            # If story is excellent (avg ≥ 8.5), override feedback with a positive remark
            if avg_score >= 8.5:
                evaluation["feedback"] = "Excellent story! Keep it up — but you can make it funnier by adding animal sounds like 'meow meow' if it's about a cat!"
            elif avg_score >= 7:
                evaluation["feedback"] = "Nice story! Just a few tweaks could make it even better."
            else:
                evaluation["feedback"] = evaluation.get("feedback", "Needs some improvement for clarity and engagement.")

    return evaluation
