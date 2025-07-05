import os
from dotenv import load_dotenv
from firebase_admin import credentials, initialize_app

# Load .env file
load_dotenv()

# Get path from env variable
firebase_key_path = os.getenv("FIREBASE_CREDENTIALS")

# Initialize Firebase
cred = credentials.Certificate(firebase_key_path)
initialize_app(cred)
