import streamlit as st
from pages.home import home_page
from pages.health_analysis import health_analysis_page
from pages.settings import settings_page

def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Home", "Health Analysis", "Settings"])

    if page == "Home":
        home_page()
    elif page == "Health Analysis":
        health_analysis_page()
    elif page == "Settings":
        settings_page()

if __name__ == "__main__":
    main()
