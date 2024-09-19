# HealthLens
Visualisation and metrics on health data


## Folder Structure

HealthLens/
│
├── app/
│   ├── main.py
│   ├── pages/
│   │   ├── dashboard.py
│   │   └── health_analysis.py
│   │
│   ├── components/
│   │   ├── charts.py
│   │   └── data_tables.py
│   │
│   └── utils/
│       ├── strava_api.py
│       ├── apple_health_api.py
│       └── data_processing.py
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