import pandas as pd
import os

def clean_column_name(name):
    return ' '.join(word.capitalize() for word in name.replace('_', ' ').split())

def process_strava_activities(activities):
    df = pd.DataFrame(activities)
    df['Distance (km)'] = df['distance'] / 1000
    df['Distance (miles)'] = df['distance'] / 1609.34
    df['Moving Time (hours)'] = df['moving_time'] // 3600
    df['Moving Time (minutes)'] = (df['moving_time'] % 3600) // 60
    df['Moving Time (seconds)'] = df['moving_time'] % 60
    df['Speed (km/h)'] = df['average_speed'] * 3.6
    df['Speed (miles/min)'] = df['average_speed'] * 2.23694 / 60
    df['Start Time'] = pd.to_datetime(df['start_date']).dt.strftime('%H:%M:%S %d-%m-%Y')
    return df

def save_activities(df):
    filepath = 'data/strava_activities.csv'
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    df.to_csv(filepath, index=False)
    print(f"Saved activities to {filepath}")
    print(f"Columns saved: {df.columns.tolist()}")

def load_activities():
    filepath = 'data/strava_activities.csv'
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        return None
    df = pd.read_csv(filepath)
    print(f"Loaded activities from {filepath}")
    print(f"Columns loaded: {df.columns.tolist()}")
    if 'Start Date' in df.columns:
        df['Start Date'] = pd.to_datetime(df['Start Date'])
    return df

def analyse_activities(df):
    summary = {
        'Total Activities': len(df),
        'Total Distance (km)': round(df['distance'].sum() / 1000) if 'distance' in df.columns else 0,
        'Total Time (hours)': round(df['moving_time'].sum() / 3600) if 'moving_time' in df.columns else 0,
        'Average Speed (km/h)': round(df['average_speed'].mean() * 3.6, 1) if 'average_speed' in df.columns else 0,
    }
    
    if 'Type' in df.columns:
        summary['Activity Types'] = df['Type'].value_counts().to_dict()
    
    return summary
