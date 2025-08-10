import os
from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv()
API_KEY = os.getenv("API_KEY")
if not API_KEY:
    raise ValueError("API_KEY not found. Please set it in the .env file.")
genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")

# Simple chat history (this example keeps memory only while the server is running)
chat_history = []

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "").strip()
    if not user_message:
        return jsonify({"error": "Message cannot be empty."}), 400

    chat_history.append({"role": "user", "content": user_message})

    # Combine last 10 messages as prompt
    recent_msgs = chat_history[-10:]
    prompt = "\n".join([m["content"] for m in recent_msgs])

    try:
        response = model.generate_content(prompt)
        bot_reply = response.text.strip()
    except Exception as e:
        bot_reply = f"[An error occurred: {e}]"

    chat_history.append({"role": "bot", "content": bot_reply})

    return jsonify({"reply": bot_reply})

if __name__ == "__main__":
    app.run(debug=True)
