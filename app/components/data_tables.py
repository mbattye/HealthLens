import streamlit as st
import pandas as pd

def display_activities_table(df):
    st.dataframe(df[['Name', 'Type', 'Distance', 'Moving Time', 'Average Speed', 'Start Date']])

def display_summary_table(summary):
    summary_df = pd.DataFrame.from_dict(summary, orient='index', columns=['Value'])
    st.table(summary_df)
