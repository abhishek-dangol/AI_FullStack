import os
import openai
import argparse


def main():
    print("Running Copy Cat!!")
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", "-i", type=str, required=True)
    args = parser.parse_args()
    user_input = args.input
    print(f"User input: {user_input}")
    result = generate_branding_snippet(user_input)
    print(result)


def generate_branding_snippet(prompt: str):
    # Load your API key from an environment variable or secret management service
    openai.api_key = os.getenv("OPENAI_API_KEY")
    enriched_prompt = f"Generate upbeat branding snippet for {prompt}: "

    response = openai.Completion.create(model="text-davinci-002", prompt=enriched_prompt, temperature=0, max_tokens=32)

    # Extract output text
    branding_text: str = response["choices"][0]["text"]
    
    # Strip whitespace
    branding_text = branding_text.strip()
    
    # Add ... to truncated statements
    last_char = branding_text[-1]
    if last_char not in {".", "!", "?"}:
        branding_text += "..."
    
    return branding_text

if __name__ == "__main__":
    main()