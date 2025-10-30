try:
    name = input("Enter your name: ").strip()
    feedback = input("Enter your feedback: ").strip()

    if not name or not feedback:
        raise ValueError("Name and feedback cannot be empty!")

except ValueError as e:
    print(f"Error: {e}")

else:
    print("\nThank you for your feedback!")
    print(f"Name: {name}")
    print(f"Feedback: {feedback}")

finally:
    print("\nFeedback session completed.")
