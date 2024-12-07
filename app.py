from flask import Flask, render_template, request, jsonify
import joblib
from pymongo import MongoClient
import openai
import pyttsx3
from flask_cors import CORS
import logging
import speech_recognition as sr
import requests
from dotenv import load_dotenv
import os

app = Flask(__name__)
CORS(app, origins=["http://localhost:3000"], supports_credentials=True)  # Enable CORS for cross-origin requests

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Load environment variables
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')
mongo_uri = os.getenv('MONGO_URI')

app.secret_key = 'your_secret_key'  # Replace with your actual secret key

# MongoDB connection
client = MongoClient(mongo_uri)
db = client['dumelahealth_db']
clinics_collection = db['clinics']

# Load the trained model
try:
    model = joblib.load('assistant_model.pkl')
    logging.info("Model loaded successfully.")
except FileNotFoundError:
    logging.error("Model file not found. Please train the model and save it as 'assistant_model.pkl'.")
    model = None

# Text-to-Speech Engine Configuration
tts_engine = pyttsx3.init()
voices = tts_engine.getProperty('voices')
tts_engine.setProperty('voice', voices[1].id)  # Use a female voice
tts_engine.setProperty('rate', 150)  # Adjust speaking rate

def speak_text(text):
    """Function to convert text to speech."""
    tts_engine.say(text)
    tts_engine.runAndWait()

# Initialize conversation context
conversation_history = [
    {"role": "system", "content": "You are a kind and empathetic healthcare assistant who provides emotional support and mental health advice."}
]

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
    try:
        lat = float(request.args.get('lat'))
        lng = float(request.args.get('lng'))
        logging.debug(f"Received lat: {lat}, lng: {lng}")
        clinics = get_nearby_clinics(lat, lng)
        logging.debug(f"Found clinics: {clinics}")
        return jsonify(clinics)
    except (TypeError, ValueError) as e:
        logging.error(f"Error in api_nearby_clinics: {e}")
        return jsonify({"error": "Invalid latitude or longitude"}), 400
    except Exception as e:
        logging.error(f"Unexpected error in api_nearby_clinics: {e}")
        return jsonify({"error": "Unable to fetch nearby clinics"}), 500

def get_nearby_clinics(lat, lng, radius=10):
    try:
        logging.debug(f"Querying clinics within {radius} km of ({lat}, {lng})")
        clinics = clinics_collection.find({
            "location": {
                "$geoWithin": {
                    "$centerSphere": [[lng, lat], radius / 6378.1]
                }
            }
        })
        clinic_list = [{
            "name": c["name"],
            "address": c["address"],
            "services": c["services"],
            "hours": c["hours"],
            "directions": c["directions"],
            "lat": c["location"]["coordinates"][1],  # Latitude
            "lng": c["location"]["coordinates"][0]   # Longitude
        } for c in clinics]
        logging.debug(f"Clinics found: {clinic_list}")
        return clinic_list
    except Exception as e:
        logging.error(f"Error in get_nearby_clinics: {e}")
        return []

@app.route('/dumela-assistant')
def dumela_assistant():
    return render_template('dumela_assistant.html')

@app.route('/start-conversation', methods=['GET'])
def start_conversation():
    # Sample response for testing
    try:
        initial_message = "Hi! I'm here to help with any healthcare concerns you have."
        conversation_history.append({"role": "assistant", "content": initial_message})
        speak_text(initial_message)
        return jsonify({"assistant": initial_message})
    except Exception as e:
        logging.error(f"Error in start-conversation: {e}")
        return jsonify({"error": str(e)}), 500

@app.route('/continue-conversation', methods=['POST'])
def continue_conversation():
    try:
        if not request.is_json:
            logging.error("Request is not JSON.")
            return jsonify({"error": "Invalid input format. JSON expected."}), 400

        # Extract user message
        user_message = request.json.get('message', '').strip()
        if not user_message:
            logging.error("Empty message received.")
            return jsonify({"error": "Message field is required."}), 400

        # Ensure the model is loaded
        if model is None:
            logging.error("Model not loaded.")
            return jsonify({"error": "Model is unavailable. Please try again later."}), 500

        # Predict response using the model
        try:
            assistant_message = model.predict([user_message])[0]
        except Exception as e:
            logging.error(f"Error during model prediction: {e}", exc_info=True)
            return jsonify({"error": "Failed to process your request."}), 500

        # Append to conversation history
        conversation_history.append({"role": "user", "content": user_message})
        conversation_history.append({"role": "assistant", "content": assistant_message})

         # Convert text-to-speech (optional)
        try:
            speak_text(assistant_message)
        except Exception as e:
            logging.warning(f"TTS Error: {e}")

        # Return response
        return jsonify({"assistant": assistant_message})

    except Exception as e:
        logging.error(f"Unhandled error in continue-conversation: {e}", exc_info=True)
        return jsonify({"error": "Internal server error", "details": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
