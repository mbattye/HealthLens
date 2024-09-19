import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Strava API credentials
STRAVA_CLIENT_ID = os.getenv('STRAVA_CLIENT_ID')
STRAVA_CLIENT_SECRET = os.getenv('STRAVA_CLIENT_SECRET')

# Add other API keys or configuration variables here as needed
