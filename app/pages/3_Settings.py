import streamlit as st
from app.utils.strava_api import StravaAPI
from app.utils.data_processing import process_strava_activities, save_activities
import logging

logging.basicConfig(filename='app.log', level=logging.INFO)

def main():
    st.title("Settings")
    st.header("Strava Authentication")

    strava_api = StravaAPI()

    # Check for the presence of a 'code' in the URL parameters
    if 'code' in st.query_params and 'strava_token' not in st.session_state:
        code = st.query_params['code']
        logging.info(f"Received code: {code}")
        try:
            token = strava_api.fetch_token(code)
            st.session_state['strava_token'] = token
            st.success("Successfully authenticated with Strava!")
            # Clear the query parameters to prevent reuse of the code
            st.query_params.clear()
            st.rerun()
        except Exception as e:
            logging.error(f"Error during authentication: {str(e)}")
            st.error("An error occurred during authentication. Please try again.")
            st.session_state.pop('strava_token', None)
    elif 'code' in st.query_params and 'strava_token' in st.session_state:
        # If we have a code but we're already authenticated, just clear the query params
        st.query_params.clear()
        st.rerun()

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
                logging.error(f"Error syncing data: {str(e)}")
                st.error(f"Error syncing data: {str(e)}")

        if st.button("Log out"):
            st.session_state.pop('strava_token', None)
            st.success("Logged out successfully.")
            st.rerun()

if __name__ == "__main__":
    main()
