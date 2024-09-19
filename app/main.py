import streamlit as st
from pages.dashboard import dashboard_page
from pages.health_analysis import health_analysis_page

def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Dashboard", "Health Analysis"])

    if page == "Dashboard":
        dashboard_page()
    elif page == "Health Analysis":
        health_analysis_page()

if __name__ == "__main__":
    main()
