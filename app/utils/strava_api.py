import requests
from requests_oauthlib import OAuth2Session

class StravaAPI:
    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret
        self.token_url = 'https://www.strava.com/oauth/token'
        self.authorize_url = 'https://www.strava.com/oauth/authorize'
        self.base_url = 'https://www.strava.com/api/v3/'

    def get_authorization_url(self):
        oauth = OAuth2Session(self.client_id, redirect_uri='YOUR_REDIRECT_URI')
        authorization_url, _ = oauth.authorization_url(self.authorize_url)
        return authorization_url

    def fetch_token(self, code):
        oauth = OAuth2Session(self.client_id, redirect_uri='YOUR_REDIRECT_URI')
        token = oauth.fetch_token(
            self.token_url,
            client_secret=self.client_secret,
            code=code
        )
        return token

    def get_athlete_activities(self, access_token, per_page=30, page=1):
        headers = {'Authorization': f'Bearer {access_token}'}
        response = requests.get(
            f'{self.base_url}athlete/activities',
            headers=headers,
            params={'per_page': per_page, 'page': page}
        )
        return response.json()

# Usage example:
# strava_api = StravaAPI('YOUR_CLIENT_ID', 'YOUR_CLIENT_SECRET')
# auth_url = strava_api.get_authorization_url()
# # Redirect user to auth_url and get the 'code' from the redirect
# token = strava_api.fetch_token('CODE_FROM_REDIRECT')
# activities = strava_api.get_athlete_activities(token['access_token'])
