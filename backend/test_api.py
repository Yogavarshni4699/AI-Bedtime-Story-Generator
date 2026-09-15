"""
Test script to verify the backend is working correctly
"""
import os
from dotenv import load_dotenv

load_dotenv()

print("=" * 50)
print("Testing AI Bedtime Story Generator Backend")
print("=" * 50)

# Test 1: Check API key
print("\n1. Checking OPENAI_API_KEY...")
api_key = os.getenv("OPENAI_API_KEY")
if not api_key or api_key in ["your_key_here", "your_openai_api_key_here"]:
    print("❌ OPENAI_API_KEY is not set or invalid!")
    print("   Please set your OpenAI API key in the .env file")
    exit(1)
else:
    print(f"✅ API key found (starts with: {api_key[:7]}...)")

# Test 2: Import modules
print("\n2. Testing imports...")
try:
    from utils import call_model
    print("✅ utils module imported successfully")
except Exception as e:
    print(f"❌ Failed to import utils: {e}")
    exit(1)

try:
    from agents import storyteller_agent, judge_agent
    print("✅ agents module imported successfully")
except Exception as e:
    print(f"❌ Failed to import agents: {e}")
    exit(1)

# Test 3: Test storyteller agent
print("\n3. Testing storyteller agent...")
try:
    test_prompt = "A very short story about a happy cat"
    print(f"   Prompt: '{test_prompt}'")
    story = storyteller_agent(test_prompt)
    print(f"✅ Story generated successfully!")
    print(f"   Story length: {len(story)} characters")
    print(f"   First 100 chars: {story[:100]}...")
except Exception as e:
    print(f"❌ Failed to generate story: {e}")
    import traceback
    traceback.print_exc()
    exit(1)

# Test 4: Test judge agent
print("\n4. Testing judge agent...")
try:
    evaluation = judge_agent(story)
    print(f"✅ Story evaluated successfully!")
    print(f"   Scores: {evaluation.get('scores', {})}")
    print(f"   Feedback: {evaluation.get('feedback', 'N/A')}")
except Exception as e:
    print(f"❌ Failed to evaluate story: {e}")
    import traceback
    traceback.print_exc()
    exit(1)

print("\n" + "=" * 50)
print("✅ All tests passed! Backend is working correctly.")
print("=" * 50)
print("\nYou can now:")
print("1. Run the API server: python api.py")
print("2. Run the CLI version: python main_cli.py")
