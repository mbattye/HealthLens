import streamlit as st

def home_page():
    st.title("Welcome to Health Data Visualization")
    st.write("This app allows you to visualize and analyze your health data from Strava.")
    
    st.header("Available Pages")
    st.write("- **Health Analysis**: View and analyze your health data")
    st.write("- **Settings**: Manage your Strava API connection")

    st.info("Please go to the Settings page to authenticate with Strava before accessing your health data.")
