import streamlit as st
import plotly.express as px
import pandas as pd

def plot_activity_types(df):
    if 'Type' not in df.columns:
        st.warning("Activity type data is not available.")
        return
    
    activity_counts = df['Type'].value_counts()
    top_activities = activity_counts.head(4)
    other_activities = activity_counts[4:].sum()
    activity_counts = top_activities.append(pd.Series({'Other': other_activities}))
    
    colors = ['#ef476f', '#ffd166', '#06d6a0', '#118ab2', '#073b4c']
    fig = px.pie(values=activity_counts.values, names=activity_counts.index, title='Activity Types', color_discrete_sequence=colors)
    st.plotly_chart(fig)

def plot_distance_over_time(df):
    fig = px.line(df, x='start_date', y='distance', title='Distance Over Time')
    st.plotly_chart(fig)

def plot_activity_heatmap(df):
    if 'Start Date' not in df.columns:
        st.warning("Activity start date data is not available.")
        return
    
    df['Start Date'] = pd.to_datetime(df['Start Date'])
    df['Weekday'] = df['Start Date'].dt.day_name()
    df['Hour'] = df['Start Date'].dt.hour
    heatmap_data = df.groupby(['Weekday', 'Hour']).size().reset_index(name='Count')
    fig = px.density_heatmap(heatmap_data, x='Hour', y='Weekday', z='Count', title='Activity Heatmap', nbinsx=24)
    st.plotly_chart(fig)

def plot_activity_duration(df):
    if 'Moving Time' not in df.columns or 'Start Date' not in df.columns:
        st.warning("Activity duration data is not available.")
        return
    
    df['Start Date'] = pd.to_datetime(df['Start Date'])
    df['Duration (hours)'] = df['Moving Time'] / 3600
    fig = px.scatter(df, x='Start Date', y='Duration (hours)', color='Type', title='Activity Duration Over Time', height=600)
    st.plotly_chart(fig)

def plot_activity_distance(df):
    if 'Distance' not in df.columns or 'Start Date' not in df.columns:
        st.warning("Activity distance data is not available.")
        return
    
    df['Start Date'] = pd.to_datetime(df['Start Date'])
    df['Distance (km)'] = df['Distance'] / 1000
    fig = px.scatter(df, x='Start Date', y='Distance (km)', color='Type', title='Activity Distance Over Time', height=600)
    st.plotly_chart(fig)

# Add more chart functions as needed
