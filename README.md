![Screenshot 2024-12-02 170022](https://github.com/user-attachments/assets/64ddba44-3711-44d8-ba26-557d02b8d4be)
# IMPLEMENTING NEURA-BOT 

## 📌 Project Overview
A Flask-based web application that integrates Google's Gemini AI to create an interactive chatbot interface. Users can input prompts and receive AI-generated responses quickly and easily.

## ✨ Features
- Simple and intuitive web interface
- Real-time AI-powered responses
- Error handling for robust user experience
- Secure API key management using environment variables

## 🛠 Tech Stack
- Flask
- Google Generative AI
- Python
- HTML/CSS

## 🚀 Installation and Setup

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Steps
1. Clone the repository
```bash
git clone https://github.com/abhijit826/NEURA-BOT.git
cd neura-bot
```

2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Configure API Key
- Create a `.env` file in the project root
- Add your Google API key:
```
GOOGLE_API_KEY=your_api_key_here
```

## 🖥 Running the Application
```bash
python app.py
```

## 🔒 Security Notes
- Never commit sensitive information like API keys
- Use environment variables for configuration
- Regularly rotate API keys

## 📄 License
This project is open-source. Please check the LICENSE file for details.


