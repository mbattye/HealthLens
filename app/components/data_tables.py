import streamlit as st
import pandas as pd

def display_summary_table(summary):
    summary_df = pd.DataFrame(list(summary.items()), columns=['Metric', 'Value'])
    st.table(summary_df)

def display_activities_table(df):
    df = df.drop(columns=['resource_state', 'athlete', 'id', 'start_date_local', 'timezone', 'utc_offset', 'location_city', 'location_state', 'location_country', 'achievement_count', 'kudos_count', 'comment_count', 'athlete_count', 'photo_count', 'map', 'trainer', 'commute', 'manual', 'private', 'visibility', 'flagged', 'gear_id', 'start_latlng', 'end_latlng', 'average_speed', 'max_speed', 'has_heartrate', 'average_heartrate', 'max_heartrate', 'heartrate_opt_out', 'display_hide_heartrate_option', 'elev_high', 'elev_low', 'upload_id', 'upload_id_str', 'external_id', 'from_accepted_tag', 'pr_count', 'total_photo_count', 'has_kudoed', 'suffer_score', 'average_watts', 'kilojoules', 'device_watts', 'average_temp'])
    st.dataframe(df)
