import streamlit as st
from app.utils.data_processing import load_activities, analyse_activities
from app.components.charts import plot_activity_types, plot_distance_over_time, plot_activity_heatmap
from app.components.data_tables import display_summary_table

def dashboard_page():
    st.title("Health Data Dashboard")

    # Load activities
    activities_df = load_activities()
    if activities_df is None:
        st.warning("No data available. Please sync your Strava data first.")
        return

    # Analyze activities
    summary = analyse_activities(activities_df)

    # Display summary
    st.header("Activity Summary")
    display_summary_table(summary)

    # Display charts
    st.header("Activity Analysis")
    col1, col2 = st.columns(2)
    with col1:
        plot_activity_types(activities_df)
    with col2:
        plot_distance_over_time(activities_df)

    st.header("Activity Patterns")
    plot_activity_heatmap(activities_df)

if __name__ == "__main__":
    dashboard_page()
