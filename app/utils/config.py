import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Strava API credentials
STRAVA_CLIENT_ID = os.getenv('STRAVA_CLIENT_ID')
STRAVA_CLIENT_SECRET = os.getenv('STRAVA_CLIENT_SECRET')
STRAVA_REDIRECT_URI = 'http://localhost:8501/Settings'  # Note the capital 'S' in Settings

# Add other API keys or configuration variables here as needed
