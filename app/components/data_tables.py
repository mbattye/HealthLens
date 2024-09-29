import streamlit as st
import pandas as pd

def display_summary_table(summary):
    summary_df = pd.DataFrame(list(summary.items()), columns=['Metric', 'Value'])
    summary_df.columns = [x.replace("_", " ").title() for x in summary_df.columns]
    # Convert 'Value' column to numeric, replacing any non-numeric values with NaN
    summary_df['Value'] = pd.to_numeric(summary_df['Value'], errors='coerce')
    
    # Round the first 3 rows to integers and the 4th row to 1 decimal place
    summary_df.loc[:2, 'Value'] = summary_df.loc[:2, 'Value'].round(0).astype(int)
    if len(summary_df) > 3:
        summary_df.loc[3, 'Value'] = summary_df.loc[3, 'Value'].round(1)
    
    # Display the table with custom styling
    st.dataframe(
        summary_df,
        hide_index=True,
        column_config={
            "Metric": st.column_config.TextColumn(
                "Metric",
                width="medium",
            ),
            "Value": st.column_config.NumberColumn(
                "Value",
                format="%.1f",
            ),
        },
    )

def display_activities_table(df):
    df = df.drop(columns=['resource_state', 'athlete', 'id', 'start_date_local', 'timezone', 'utc_offset', 'location_city', 'location_state', 'location_country', 'achievement_count', 'kudos_count', 'comment_count', 'athlete_count', 'photo_count', 'map', 'trainer', 'commute', 'manual', 'private', 'visibility', 'flagged', 'gear_id', 'start_latlng', 'end_latlng', 'average_speed', 'max_speed', 'has_heartrate', 'average_heartrate', 'max_heartrate', 'heartrate_opt_out', 'display_hide_heartrate_option', 'elev_high', 'elev_low', 'upload_id', 'upload_id_str', 'external_id', 'from_accepted_tag', 'pr_count', 'total_photo_count', 'has_kudoed', 'suffer_score', 'average_watts', 'kilojoules', 'device_watts', 'average_temp'])
    df.columns = [x.replace("_", " ").title() for x in df.columns]
    st.dataframe(df)
