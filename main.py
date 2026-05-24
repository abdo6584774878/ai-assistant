from dotenv import load_dotenv
from google import genai
from google.genai import types
import os

# Load environment variables from .env file
load_dotenv()
api_key = os.environ.get("GEMINI-API-KEY")
# Initialize the GenAI client with the API key from environment variables
client = genai.Client(api_key=api_key)


def ai_assistant():
    print("assistant initialized Type 'exit' to quit.\n")
    config = types.GenerateContentConfig(
        system_instruction="Your are a helpful and witty coding assistant. Keep your answers concise, practical, and beginner-friendly "
    )
    while True:
        user_input = input("User: ")
        if user_input.lower() == "exit":
            print("Exiting assistant. Goodbye!")
            break
        if not user_input.strip():
            continue
        try:
            print("Assistant is thinking...")
            response = client.models.generate_content(
                model="gemini-2.5-flash", contents=[user_input], config=config
            )
            print(f"\nAssistant: {response.text}\n")
            print("-" * 30)
        except Exception as e:
            print(f"\nAn error occurred: {e}\n")


if __name__ == "__main__":
    ai_assistant()
