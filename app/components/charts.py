import streamlit as st
import plotly.express as px
import pandas as pd

custom_colors = {
    'Run': '#ef476f',
    'Ride': '#ffd166',
    'Swim': '#06d6a0',
    'Walk': '#118ab2',
    'Hike': '#073b4c',
    'Workout': '#84a59d',
    'WeightTraining': '#f28482',
    'Yoga': '#f5cac3',
    'RockClimbing': '#84a59d',
    'Kayaking': '#f6bd60',
    # Add more activity types and colors as needed
}

def plot_activity_types(df):
    if 'type' not in df.columns:
        st.warning("Activity type data is not available.")
        return
    
    activity_counts = df['type'].value_counts()
    top_activities = activity_counts.head(4)
    other_activities = activity_counts[4:].sum()
    # activity_counts = top_activities.append(pd.Series({'Other': other_activities}))
    activity_counts = pd.concat([top_activities, pd.Series({'Other': other_activities})])

    colors = ['#ef476f', '#ffd166', '#06d6a0', '#118ab2', '#073b4c']
    fig = px.pie(values=activity_counts.values, names=activity_counts.index, title='Activity Types', color_discrete_sequence=colors)
    st.plotly_chart(fig)

def plot_distance_over_time(df):
    fig = px.line(df, x='start_date', y='distance', title='Distance Over Time')
    st.plotly_chart(fig)

def plot_activity_heatmap(df):
    if 'start_date' not in df.columns:
        st.warning("Activity start date data is not available.")
        return
    
    df['start_date'] = pd.to_datetime(df['start_date'])
    df['weekday'] = df['start_date'].dt.day_name()
    df['hour'] = df['start_date'].dt.hour
    heatmap_data = df.groupby(['weekday', 'hour']).size().reset_index(name='Count')
    fig = px.density_heatmap(heatmap_data, x='hour', y='weekday', z='Count',\
                             title='Activity Heatmap',\
                             nbinsx=24)
    fig.update_layout(
    xaxis_title='Day',
    yaxis_title='Month'
    )
    fig.update_coloraxes(colorbar_title_text='Count')
    
    st.plotly_chart(fig)

def plot_activity_duration(df):
    if 'moving_time' not in df.columns or 'start_date' not in df.columns:
        st.warning("Activity duration data is not available.")
        return
    
    df['start_date'] = pd.to_datetime(df['start_date'])
    df['duration_hours'] = df['moving_time'] / 3600
    fig = px.scatter(df, x='start_date', y='duration_hours', color='type', title='Activity Duration Over Time', height=600, color_discrete_map=custom_colors)
    
    fig.update_layout(
    xaxis_title='Date',
    yaxis_title='Duration (hours)'
    )
    fig.update_layout(legend_title_text='Activity Type')
    
    st.plotly_chart(fig)

def plot_activity_distance(df):
    if 'distance' not in df.columns or 'start_date' not in df.columns:
        st.warning("Activity distance data is not available.")
        return
    
    df['start_date'] = pd.to_datetime(df['start_date'])
    df['distance_km'] = df['distance'] / 1000
    fig = px.scatter(df, x='start_date', y='distance_km', color='type', title='Activity Distance Over Time', height=600, color_discrete_map=custom_colors)

    fig.update_layout(
    xaxis_title='Date',
    yaxis_title='Distance (km)'
    )
    fig.update_layout(legend_title_text='Activity Type')
    
    st.plotly_chart(fig)

# Add more chart functions as needed
