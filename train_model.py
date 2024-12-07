import joblib
from pymongo import MongoClient
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
mongo_uri = os.getenv('MONGO_URI')

# MongoDB connection
client = MongoClient(mongo_uri)
db = client['dumelahealth_db']
training_collection = db['training_data']

# Fetch training data from MongoDB
training_data = list(training_collection.find({}))

# Prepare the data
user_inputs = [data['user_input'] for data in training_data]
responses = [data['response'] for data in training_data]

# Create a text classification model
model = make_pipeline(TfidfVectorizer(), LogisticRegression())
model.fit(user_inputs, responses)

# Save the model
joblib.dump(model, 'assistant_model.pkl')
print("Model trained and saved successfully.")