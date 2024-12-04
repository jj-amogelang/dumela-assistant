# app.py
from flask import Flask, render_template, request, jsonify
import pandas as pd
from database import get_nearby_clinics, clinics_collection
from pymongo import MongoClient
import openai
import pyttsx3
from flask_cors import CORS
import logging

app = Flask(__name__)
CORS(app)  # Enable CORS for cross-origin requests

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# OpenAI API Key
openai.api_key = "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"

app.secret_key = 'your_secret_key'  # Replace with your actual secret key
app.config['UPLOAD_FOLDER'] = 'uploads/'

# MongoDB connection
client = MongoClient('mongodb://localhost:27017/')  # Replace with your MongoDB URI
db = client['dumelahealth_db']
clinics_collection = db['clinics']

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get-started')
def get_started():
    return render_template('get_started.html')

@app.route('/chat-assistant')
def chat_assistant():
    return render_template('chat_assistant.html')

@app.route('/nearby-clinics')
def nearby_clinics():
    return render_template('nearby_clinics.html')

@app.route('/api/nearby-clinics')
def api_nearby_clinics():
    lat = float(request.args.get('lat'))
    lng = float(request.args.get('lng'))

    clinics = get_nearby_clinics(lat, lng)

    return jsonify(clinics)

# DUMELA-ASSISTANT

# Text-to-Speech Engine
tts_engine = pyttsx3.init()

# Initialize conversation context
conversation_history = [
    {"role": "system", "content": "You are a compassionate healthcare assistant. Respond empathetically and provide helpful advice."}
]

# Serve the assistant.html page
@app.route('/dumela-assistant')
def dumela_assistant():
    return render_template('dumela_assistant.html')

# Endpoint to start the conversation
@app.route('/start-conversation', methods=['GET'])
def start_conversation():
    try:
        initial_message = "Hello, how are you feeling today?"
        conversation_history.append({"role": "assistant", "content": initial_message})
        tts_engine.say(initial_message)
        tts_engine.runAndWait()
        return jsonify({"assistant": initial_message})
    except Exception as e:
        logging.error(f"Error in start-conversation: {e}")
        return jsonify({"error": str(e)}), 500

# Endpoint to continue the conversation
@app.route('/continue-conversation', methods=['POST'])
def continue_conversation():
    user_input = request.json.get('message')
    if not user_input:
        return jsonify({"error": "No input provided"}), 400

    try:
        # Add user input to conversation history
        conversation_history.append({"role": "user", "content": user_input})

        # Generate response using OpenAI GPT
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=conversation_history
        )
        assistant_response = response['choices'][0]['message']['content']

        # Add assistant response to conversation history
        conversation_history.append({"role": "assistant", "content": assistant_response})

        # Speak the assistant's response
        tts_engine.say(assistant_response)
        tts_engine.runAndWait()

        return jsonify({"assistant": assistant_response})
    except Exception as e:
        logging.error(f"Error in continue-conversation: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
