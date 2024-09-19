import streamlit as st
import pandas as pd

def display_activities_table(df):
    st.dataframe(df[['start_date', 'name', 'type', 'distance', 'moving_time', 'average_speed']])

def display_summary_table(summary):
    summary_df = pd.DataFrame([summary])
    st.table(summary_df.T)
