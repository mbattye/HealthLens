import streamlit as st
import plotly.express as px

def plot_activity_types(df):
    activity_counts = df['type'].value_counts()
    fig = px.pie(values=activity_counts.values, names=activity_counts.index, title='Activity Types')
    st.plotly_chart(fig)

def plot_distance_over_time(df):
    fig = px.line(df, x='start_date', y='distance', title='Distance Over Time')
    st.plotly_chart(fig)

def plot_activity_heatmap(df):
    df['weekday'] = df['start_date'].dt.day_name()
    df['hour'] = df['start_date'].dt.hour
    heatmap_data = df.groupby(['weekday', 'hour']).size().reset_index(name='count')
    fig = px.density_heatmap(heatmap_data, x='hour', y='weekday', z='count', title='Activity Heatmap')
    st.plotly_chart(fig)
