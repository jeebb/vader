import argparse
import openai

def main():
    parser = argparse.ArgumentParser(description="Vader: A command-line application to interact with OpenAI's API.")
    parser.add_argument("prompt", type=str, help="The prompt to send to OpenAI's API.")
    args = parser.parse_args()

    response = openai.Completion.create(
        engine="davinci",
        prompt=args.prompt,
        max_tokens=50
    )

    print(response.choices[0].text.strip())

if __name__ == "__main__":
    main()
