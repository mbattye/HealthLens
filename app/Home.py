import streamlit as st

def main():
    st.title("Welcome to HealthLens")
    st.write("Visualize and analyze your health data from Strava.")
    
    st.header("Available Pages")
    st.write("- **Analysis**: View and analyze your health data")
    st.write("- **Dashboard**: Quick overview of your health metrics")
    st.write("- **Settings**: Manage your Strava API connection")

    st.info("Please go to the Settings page to authenticate with Strava before accessing your health data.")

if __name__ == "__main__":
    main()
