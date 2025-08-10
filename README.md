# 💬 Gemini Chatbot - Flask + TailwindCSS

A chatbot project integrated with Google **Gemini API** featuring a modern interface.  
Works with Flask backend and TailwindCSS-powered frontend.  
Includes dark/light theme support, typing indicator animation, and chat history.

---

## 🚀 Features
- **Modern and responsive UI**  
- **Dark/Light theme support**  
- **Google Gemini API (gemini-2.5-flash) integration**  
- **Chat history (temporary, resets when server restarts)**  
- **Typing indicator animation**  
- Quick message sending with Enter key  
- Flask backend + Vanilla JS frontend structure

---

## 📂 Project Structure
```plaintext
templates/
 └── index.html      # Frontend UI file
.env                 # API key stored here
.gitignore
app.py               # Flask backend
main.py              # Alternative startup file
requirements.txt     # Python dependencies
```

---

## 🔧 Installation and Running

### 1️⃣ Clone the repository
```bash
git clone https://github.com/Onursafa0/gemini-chatbot.git
cd gemini-chatbot
```

### 2️⃣ Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Set the API key  
Add a `.env` file to the project root directory containing:
```env
API_KEY=YOUR_GEMINI_API_KEY
```

> You can get your Google Gemini API key from [Google AI Studio](https://aistudio.google.com/).

### 5️⃣ Run the app
```bash
python app.py
```
Then open your browser and go to:  
```
http://127.0.0.1:5000
```

---

## 🛠 Technologies Used
- **Backend:** [Flask](https://flask.palletsprojects.com/)  
- **Frontend:** HTML, Vanilla JS, [TailwindCSS](https://tailwindcss.com/)  
- **API:** [Google Generative AI - Gemini](https://ai.google.dev/gemini-api)  
- **Other:** python-dotenv

---

## 📜 License  
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
