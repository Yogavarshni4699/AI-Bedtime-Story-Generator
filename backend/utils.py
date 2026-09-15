import os
import openai
from dotenv import load_dotenv

load_dotenv()

def call_model(prompt: str, max_tokens=3000, temperature=0.1) -> str:
    """
    Calls OpenAI API with the given prompt and parameters.

    Args:
        prompt: The prompt to send to the model
        max_tokens: Maximum tokens in the response
        temperature: Controls randomness (0-1)

    Returns:
        The model's response as a string
    """
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key or api_key == "your_key_here" or api_key == "your_openai_api_key_here":
        raise ValueError("OPENAI_API_KEY is not set or is invalid. Please set it in the .env file.")

    openai.api_key = api_key

    try:
        resp = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            stream=False,
            max_tokens=max_tokens,
            temperature=temperature,
        )
        return resp.choices[0].message["content"]  # type: ignore
    except Exception as e:
        print(f"OpenAI API Error: {str(e)}")
        raise
