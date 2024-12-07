from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
mongo_uri = os.getenv('MONGO_URI')

# MongoDB connection
client = MongoClient(mongo_uri)
db = client['dumelahealth_db']
training_collection = db['training_data']

# Sample training data
training_data = [
    {
        "user_input": "hi",
        "response": "Hello, what can I help you with today?"
    },
    {
        "user_input": "I dislocated my shoulder",
        "response": "That sounds painful. First, try to keep your arm as still as possible to avoid further injury. You should avoid trying to pop it back into place yourself, as this could cause more damage. Apply an ice pack to reduce swelling. I strongly recommend going to the nearest hospital or an orthopedic clinic for professional treatment. Would you like me to give you directions to the nearest hospital?"
    },
    {
        "user_input": "yes, I would like directions to the nearest hospital",
        "response": "Sure, I will check your location and Zip code so I can find the closest hospital for you."
    },
    {
        "user_input": "I have a headache",
        "response": "I’m sorry you’re dealing with a headache. For a mild headache, staying hydrated and resting in a quiet room might help. However, if the headache is severe, frequent, or accompanied by symptoms like vision changes or nausea, you should visit a general or neurological clinic. Would you like directions to a clinic nearby?"
    },
    {
        "user_input": "I have a fever",
        "response": "A fever can indicate an infection. Rest, drink plenty of fluids, and monitor your temperature. For persistent or high fevers, I recommend visiting an urgent care clinic or a general practitioner. Would you like help finding a nearby clinic?"
    },
    {
        "user_input": "I feel anxious all the time",
        "response": "Anxiety can be tough to deal with. Breathing exercises, mindfulness, or talking to someone you trust might help. For ongoing or severe anxiety, I recommend visiting a mental health clinic or seeing a counselor. Would you like me to help find a clinic near you?"
    },
    {
        "user_input": "I cut my finger while cooking",
        "response": "I'm sorry to hear that! Rinse the cut under clean running water, apply pressure to stop bleeding, and cover it with a sterile bandage. For deep cuts or if bleeding doesn’t stop, you should visit an urgent care clinic. Would you like directions to the nearest one?"
    },
    {
        "user_input": "I think I have a heart problem",
        "response": "Heart issues are serious. If you’re experiencing chest pain, shortness of breath, or dizziness, seek emergency care immediately. Otherwise, a cardiology clinic is the best place for specialized evaluation. Would you like directions to a nearby cardiology clinic?"
    },
    {
        "user_input": "I can't sleep at night",
        "response": "Sleep issues can be caused by stress, poor sleep hygiene, or underlying conditions. For persistent problems, a sleep clinic or a general practitioner might help. Would you like me to locate a clinic for you?"
    },
    {
        "user_input": "I have stomach pain",
        "response": "Stomach pain can result from various causes, including indigestion or more serious conditions. If the pain is severe or lasts more than a day, visit a gastroenterology clinic or a general practitioner. Would you like me to assist with finding a clinic?"
    }
    # Add more training data as needed
]

# Insert training data into MongoDB
try:
    training_collection.insert_many(training_data)
    print("Training data inserted successfully.")
except Exception as e:
    print(f"Error inserting training data: {e}")