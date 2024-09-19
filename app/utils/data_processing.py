import pandas as pd
import os

def process_strava_activities(activities):
    df = pd.DataFrame(activities)
    df['start_date'] = pd.to_datetime(df['start_date'])
    df['distance'] = df['distance'] / 1000  # Convert to kilometers
    df['moving_time'] = df['moving_time'] / 60  # Convert to minutes
    return df

def save_activities(df, filename='strava_activities.csv'):
    filepath = os.path.join('data', filename)
    df.to_csv(filepath, index=False)

def load_activities(filename='strava_activities.csv'):
    filepath = os.path.join('data', filename)
    if os.path.exists(filepath):
        return pd.read_csv(filepath, parse_dates=['start_date'])
    return None

def analyse_activities(df):
    summary = {
        'total_activities': len(df),
        'total_distance': df['distance'].sum(),
        'total_time': df['moving_time'].sum(),
        'avg_speed': df['average_speed'].mean(),
        'activities_by_type': df['type'].value_counts().to_dict()
    }
    return summary
