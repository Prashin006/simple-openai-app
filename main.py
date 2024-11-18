from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve the OpenAI API key from the environment
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def chat_with_gpt(prompt):
    """
    Sends a user prompt to OpenAI's GPT model and returns the response.
    """
    try:
        # Correct method call
        response = client.chat.completions.create(
            model="gpt-4o", messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        # Provide detailed feedback if an error occurs
        return f"Error communicating with OpenAI API: {e}"


if __name__ == "__main__":
    print("Chatbot: Hello! Type 'quit', 'exit', or 'bye' to end the chat.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            print("Chatbot: Goodbye!")
            break
        response = chat_with_gpt(user_input)
        print("Chatbot:", response)
