import streamlit as st
from app.utils.strava_api import StravaAPI
from app.utils.data_processing import process_strava_activities, save_activities, load_activities, analyse_activities
from app.components.data_tables import display_activities_table, display_summary_table

def health_analysis_page():
    st.title("Health Data Analysis")

    # Initialize Strava API (you'll need to handle authentication)
    strava_api = StravaAPI()

    # Load or fetch activities
    activities_df = load_activities()
    if activities_df is None:
        # Fetch new data (you'll need to handle authentication and token management)
        token = st.session_state.get('strava_token')
        if token:
            activities = strava_api.get_athlete_activities(token['access_token'])
            activities_df = process_strava_activities(activities)
            save_activities(activities_df)
        else:
            st.warning("Please authenticate with Strava")
            return

    # Analyze activities
    summary = analyze_activities(activities_df)

    # Display summary
    st.header("Activity Summary")
    display_summary_table(summary)

    # Display activities table
    st.header("Recent Activities")
    display_activities_table(activities_df)

if __name__ == "__main__":
    health_analysis_page()
