from app.utils.config import STRAVA_CLIENT_ID, STRAVA_CLIENT_SECRET, STRAVA_REDIRECT_URI
import requests
from requests_oauthlib import OAuth2Session
import logging

class StravaAPI:
    def __init__(self):
        self.client_id = STRAVA_CLIENT_ID
        self.client_secret = STRAVA_CLIENT_SECRET
        self.redirect_uri = STRAVA_REDIRECT_URI
        self.token_url = 'https://www.strava.com/oauth/token'
        self.authorize_url = 'https://www.strava.com/oauth/authorize'
        self.base_url = 'https://www.strava.com/api/v3/'

    def get_authorization_url(self):
        oauth = OAuth2Session(
            self.client_id, 
            redirect_uri=self.redirect_uri,
            scope=['read,activity:read_all']
        )
        authorization_url, _ = oauth.authorization_url(self.authorize_url)
        return authorization_url

    def fetch_token(self, code):
        data = {
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'code': code,
            'grant_type': 'authorization_code'
        }
        try:
            response = requests.post(self.token_url, data=data)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logging.error(f"Error fetching token: {str(e)}")
            logging.error(f"Response content: {response.text}")
            raise

    def refresh_token(self, refresh_token):
        data = {
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'refresh_token': refresh_token,
            'grant_type': 'refresh_token'
        }
        try:
            response = requests.post(self.token_url, data=data)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logging.error(f"Error refreshing token: {str(e)}")
            logging.error(f"Response content: {response.text}")
            raise

    def get_athlete_activities(self, access_token, per_page=30, page=1):
        headers = {'Authorization': f'Bearer {access_token}'}
        try:
            response = requests.get(
                f'{self.base_url}athlete/activities',
                headers=headers,
                params={'per_page': per_page, 'page': page}
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logging.error(f"Error fetching activities: {str(e)}")
            logging.error(f"Response content: {response.text}")
            raise

    def get_all_athlete_activities(self, access_token):
        all_activities = []
        page = 1
        while True:
            activities = self.get_athlete_activities(access_token, per_page=100, page=page)
            if not activities:
                break
            all_activities.extend(activities)
            page += 1
        return all_activities

# Usage example:
# strava_api = StravaAPI()
# auth_url = strava_api.get_authorization_url()
# # Redirect user to auth_url and get the 'code' from the redirect
# token = strava_api.fetch_token('CODE_FROM_REDIRECT')
# activities = strava_api.get_athlete_activities(token['access_token'])
