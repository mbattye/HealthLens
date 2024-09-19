import pandas as pd
import os

def clean_column_name(name):
    return ' '.join(word.capitalize() for word in name.replace('_', ' ').split())

def process_strava_activities(activities):
    df = pd.DataFrame(activities)
    df.columns = [clean_column_name(col) for col in df.columns]
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
        'Total Activities': len(df),
        'Total Distance (km)': df['Distance'].sum() / 1000,
        'Total Time (hours)': df['Moving Time'].sum() / 3600,
        'Average Speed (km/h)': df['Average Speed'].mean() * 3.6,
    }
    return {clean_column_name(k): v for k, v in summary.items()}
