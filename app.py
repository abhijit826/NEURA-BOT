from flask import Flask, render_template, request, redirect, url_for
import google.generativeai as genai  # type: ignore
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Create Flask app
app = Flask(__name__)

# Define your 404 error handler to redirect to the index page
@app.errorhandler(404)
def page_not_found(e):
    return redirect(url_for('index'))

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        try:
            # Retrieve API key from environment variable
            my_api_key_gemini = os.getenv('GEMINI_API_KEY')
            
            # Explicitly configure the API key
            genai.configure(api_key=my_api_key_gemini)
            
            # Create Gemini model
            model = genai.GenerativeModel('gemini-pro')
            
            prompt = request.form['prompt']
            question = prompt
            
            # Generate response
            response = model.generate_content(question)
            
            if response.text:
                return response.text
            else:
                return "Sorry, but I think our Neura didn't want to answer that!"
        except Exception as e:
            return f"Sorry, but an error occurred: {str(e)}"
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)