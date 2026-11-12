from ai_mlops_hands_on_exercise.agent import ask_agent


def main():
    print("Bank Marketing AI Assistant")
    print("Type 'exit' to quit.")

    while True:
        question = input("\nYou: ").strip()

        if question.lower() == "exit":
            break

        if not question:
            continue

        try:
            print(f"\nClaude: {ask_agent(question)}")
        except Exception as error:
            print(f"Request failed: {type(error).__name__}")


if __name__ == "__main__":
    main()
