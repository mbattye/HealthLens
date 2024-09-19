import streamlit as st
from app.utils.data_processing import load_activities, analyse_activities
from app.components.data_tables import display_activities_table, display_summary_table

def main():
    st.title("Analysis")

    if 'strava_token' not in st.session_state:
        st.warning("Please authenticate with Strava in the Settings page before accessing your health data.")
        return

    activities_df = load_activities()
    if activities_df is None:
        st.info("No data available. Please sync your Strava data in the Settings page.")
        return

    summary = analyse_activities(activities_df)

    st.header("Activity Summary")
    display_summary_table(summary)

    st.header("Recent Activities")
    display_activities_table(activities_df)

if __name__ == "__main__":
    main()
