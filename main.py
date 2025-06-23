
def generate_outputs(input_text):
    prompts = {
        "Formal": f"Rewrite this professionally: {input_text}",
        "Friendly": f"Make this sound casual and friendly: {input_text}",
        "Motivational": f"Turn this into a motivational message: {input_text}",
        "Funny": f"Make this sentence sound like a joke: {input_text}"
    }

    print("\nTone Changer Outputs:\n")
    for tone, prompt in prompts.items():
        print(f"{tone} Tone Prompt: {prompt}")
        print(f">>> [AI Output Placeholder for {tone}]\n")

def main():
    print("=== Tone Changer Prompt Engineering Tool ===")
    user_input = input("Enter your sentence: ")
    generate_outputs(user_input)

if __name__ == "__main__":
    main()
