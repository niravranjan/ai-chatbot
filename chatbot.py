import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.environ.get("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

def chat_with_ai():
    print("AI Chatbot started! (type 'exit' to quit)\n")
    messages = [
        {"role": "system", "content": "You are a helpful and friendly assistant."}
    ]

    while True:
        user_input = input("You: ")
        if user_input.lower() in ("exit", "quit"):
            print("Bye! See you next time.")
            break

        messages.append({"role": "user", "content": user_input})

        response = client.chat.completions.create(
            model="gemini-2.5-flash",
            messages=messages
        )

        reply = response.choices[0].message.content
        print("AI:", reply)
        messages.append({"role": "assistant", "content": reply})

if __name__ == "__main__":
    chat_with_ai()