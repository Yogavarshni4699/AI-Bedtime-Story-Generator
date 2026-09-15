from agents import storyteller_agent, judge_agent

"""
Before submitting the assignment, describe here in a few sentences what you would have built next if you spent 2 more hours on this project:

"""


def feedback_loop(user_prompt):
    """
    Full verbose feedback workflow for debugging and clarity.
    Prints every step so you can see the system flow in real time.

    Args:
        user_prompt: The user's story request

    Returns:
        The final story after all feedback loops
    """

    print("\n🪄 STEP 1: Storyteller is creating the first story...")
    story = storyteller_agent(user_prompt)
    print("\n🌙 --- INITIAL STORY --- 🌙\n")
    print(story)

    print("\n🧠 STEP 2: Judge is evaluating the story...")
    evaluation = judge_agent(story)
    judge_feedback = evaluation.get("feedback", "")
    print("\n📊 --- JUDGE EVALUATION --- 📊")
    print("Scores:", evaluation.get("scores", {}))
    print("Feedback:", judge_feedback)

    print("\n🪄 STEP 3: Storyteller is revising the story using judge feedback...")
    story = storyteller_agent(user_prompt, feedback=judge_feedback)
    print("\n🌈 --- REVISED STORY AFTER JUDGE FEEDBACK --- 🌈\n")
    print(story)

    print("\n💬 STEP 4: Asking for user feedback...")
    user_feedback = input("\nWould you like to suggest any changes? (Press Enter to skip): ")

    if user_feedback.strip():
        print("\n🔁 STEP 5: Storyteller is revising again based on user feedback...")
        story = storyteller_agent(user_prompt, feedback=user_feedback)
        print("\n✨ --- STORY AFTER USER FEEDBACK --- ✨\n")
        print(story)

        print("\n🧑‍⚖️ STEP 6: Judge is re-evaluating the final story...")
        reevaluation = judge_agent(story)
        print("\n📊 --- FINAL EVALUATION --- 📊")
        print("Scores:", reevaluation.get("scores", {}))
        print("Feedback:", reevaluation.get("feedback", ""))

    else:
        print("\n✅ No user feedback given. Using the judged version as the final story.")

    print("\n🌟 --- FINAL STORY OUTPUT --- 🌟\n")
    print(story)
    print("\n🎉 Flow complete! Story generation, review, and refinement finished.\n")

    return story


def main():
    """
    Entry point for the AI Bedtime Story Generator.
    Prompts the user for a story idea and runs the full feedback loop:
    Storyteller → Judge → (User Feedback) → Judge again → Final Story.
    """
    print("🌙 Welcome to the AI Bedtime Story Generator!")

    user_input = input("What kind of story do you want to hear? ")
    feedback_loop(user_input)  # Run the complete story feedback workflow

    print("\n💤 Thanks for using the AI Storyteller! Sweet dreams! 🌟")


if __name__ == "__main__":
    main()
