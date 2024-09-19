# HealthLens
Visualisation and metrics on health data


## Folder Structure

HealthLens/
│
├── app/
│   ├── Home.py
│   ├── pages/
│   │   ├── __init__.py
│   │   ├── 1_Analysis.py
│   │   ├── 2_Settings.py
│   │   └── 2_Dashboard.py
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── config.py
│   │   ├── strava_api.py
│   │   ├── apple_health_api.py
│   │   └── data_processing.py
│   └── components/
│       ├── __init__.py
│       ├── charts.py
│       └── data_tables.py
│
├── data/
│   └── .gitkeep
│
├── tests/
│   └── test.py
│
├── .streamlit/
│   └── config.toml
│
├── requirements.txt
├── README.md
├── .gitignore
├── LICENSE
└── Procfile  # For Heroku deployment (optional)