import streamlit as st
from app.utils.strava_api import StravaAPI
from app.utils.data_processing import process_strava_activities, save_activities
import logging
import time

# Set up logging
logging.basicConfig(filename='app.log', level=logging.ERROR)

def main():
    st.title("Settings")
    st.header("Strava Authentication")

    strava_api = StravaAPI()

    # Check for the presence of a 'code' in the URL parameters
    if 'code' in st.query_params:
        code = st.query_params['code']
        try:
            token = strava_api.fetch_token(code)
            st.session_state['strava_token'] = token
            st.query_params.clear()
            st.success("Successfully authenticated with Strava!")
            st.rerun()
        except Exception as e:
            logging.error(f"Error fetching token: {str(e)}")
            st.error("An error occurred during authentication. Please try again.")
            st.session_state.pop('strava_token', None)  # Ensure token is removed if fetch fails

    if 'strava_token' not in st.session_state:
        auth_url = strava_api.get_authorization_url()
        st.write("Please authenticate with Strava to access your data.")
        st.markdown(f"[Authenticate with Strava]({auth_url})")
    else:
        st.success("You are authenticated with Strava.")
        if st.button("Sync Strava Data"):
            try:
                token = st.session_state['strava_token']
                activities = strava_api.get_all_athlete_activities(token['access_token'])
                activities_df = process_strava_activities(activities)
                save_activities(activities_df)
                st.success(f"Strava data synced successfully! {len(activities)} activities retrieved.")
            except Exception as e:
                st.error(f"Error syncing data: {str(e)}")

        if st.button("Log out"):
            st.session_state.pop('strava_token', None)
            st.success("Logged out successfully.")
            st.rerun()

if __name__ == "__main__":
    main()
