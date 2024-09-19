import streamlit as st
from app.utils.strava_api import StravaAPI
from app.utils.data_processing import process_strava_activities, save_activities

def settings_page():
    st.title("Settings")
    st.header("Strava Authentication")

    strava_api = StravaAPI()

    if 'code' in st.query_params:
        code = st.query_params['code']
        try:
            token = strava_api.fetch_token(code)
            st.session_state['strava_token'] = token
            st.query_params.clear()
            st.success("Successfully authenticated with Strava!")
            st.rerun()
        except Exception as e:
            st.error(f"Error fetching token: {str(e)}")

    if 'strava_token' not in st.session_state:
        auth_url = strava_api.get_authorization_url()
        st.write("Please authenticate with Strava to access your data.")
        st.markdown(f"[Authenticate with Strava]({auth_url})")
    else:
        st.success("You are authenticated with Strava.")
        if st.button("Sync Strava Data"):
            token = st.session_state['strava_token']
            activities = strava_api.get_athlete_activities(token['access_token'])
            activities_df = process_strava_activities(activities)
            save_activities(activities_df)
            st.success("Strava data synced successfully!")

        if st.button("Log out"):
            del st.session_state['strava_token']
            st.success("Logged out successfully.")
            st.rerun()
