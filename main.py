import os
import google.generativeai as genai
from dotenv import load_dotenv
import platform
import subprocess

def configure_api():
    load_dotenv()
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY not found. Please set it in the .env file.")
    genai.configure(api_key=api_key)

class GeminiChatBot:
    def __init__(self, model_name="gemini-2.5-flash", max_history=5):
        self.model = genai.GenerativeModel(model_name)
        self.chat_history = []  # List: [{"role": "user", "content": "..."}, {"role": "bot", "content": "..."}]
        self.max_history = max_history

    def generate_response(self, user_input):
        # Combine message history and new user message
        self.chat_history.append({"role": "user", "content": user_input})

        # Prepare prompt with limited history (last max_history pairs)
        prompt_messages = []
        # Only take last max_history * 2 (user + bot) messages
        recent_history = self.chat_history[-self.max_history*2:]
        for msg in recent_history:
            prompt_messages.append(msg["content"])

        prompt = "\n".join(prompt_messages)

        try:
            response = self.model.generate_content(prompt)
            bot_reply = response.text.strip()
        except Exception as e:
            bot_reply = f"[An error occurred: {e}]"

        self.chat_history.append({"role": "bot", "content": bot_reply})
        return bot_reply

def clear_console():
    if platform.system() == "Windows":
        subprocess.call("cls", shell=True)
    else:
        subprocess.call("clear", shell=True)

def print_help():
    print("""
Commands:
  exit     - Exit the program
  clear    - Clear the console
  help     - Show this help message
""")

def main():
    print("🤖 Gemini Text Chat (Type 'exit' to quit, 'help' for help)")

    configure_api()
    bot = GeminiChatBot()

    while True:
        user_input = input("You: ").strip()
        if not user_input:
            print("Please type something.")
            continue

        cmd = user_input.lower()

        if cmd == "exit":
            print("AI: See you later!")
            break
        elif cmd == "clear":
            clear_console()
            continue
        elif cmd == "help":
            print_help()
            continue

        response = bot.generate_response(user_input)
        print("AI:", response)

if __name__ == "__main__":
    main()
