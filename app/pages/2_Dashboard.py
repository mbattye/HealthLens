import streamlit as st
import pandas as pd
from app.utils.data_processing import load_activities, analyse_activities
from app.components.charts import plot_activity_types, plot_activity_duration, plot_activity_distance, plot_activity_heatmap

def main():
    st.title("Activity Dashboard")

    activities_df = load_activities()

    if activities_df is None or activities_df.empty:
        st.warning("No activity data available. Please sync your Strava data in the Settings page.")
        return

    st.write("## Activity Summary")
    summary = analyse_activities(activities_df)
    st.metric("Total Activities", summary['Total Activities'])
    st.metric("Total Distance (km)", summary['Total Distance (km)'])
    st.metric("Total Time (hours)", summary['Total Time (hours)'])
    st.metric("Average Speed (km/h)", summary['Average Speed (km/h)'])

    st.write("## Activity Types")
    plot_activity_types(activities_df)

    st.write("## Activity Duration")
    plot_activity_duration(activities_df)

    st.write("## Activity Distance")
    plot_activity_distance(activities_df)

    st.write("## Activity Heatmap")
    plot_activity_heatmap(activities_df)

    # Add more visualizations as needed

if __name__ == "__main__":
    main()
