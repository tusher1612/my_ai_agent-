import os
import sys
from dotenv import load_dotenv
from google import genai


def main():
        load_dotenv()
        api_key = os.environ.get("GEMINI_API_KEY")
        client = genai.Client(api_key=api_key)
        if len(sys.argv) < 2:
            print("Please provide a prompt as a command-line argument.")
            sys.exit(1)
        prompt = sys.argv[1]    
        response = client.models.generate_content(
        model='gemini-2.0-flash-001', contents=prompt
        )
        print(response.text)
        if response.usage_metadata is not None:
            print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
            print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
        else:
            print("Usage metadata is not available in the response.")
main()