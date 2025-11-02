# dashboard.py - Main Application File
import streamlit as st
import json

# Import the UI components from the new folder
from ui_components.header import display_header_and_about
from ui_components.radar import display_risk_radar
from ui_components.correlator import display_cause_effect_correlator
from ui_components.forecaster import display_dynamic_forecaster
from ui_components.news import display_on_the_radar
from ui_components.insights import display_key_insights

def inject_custom_css():
    st.markdown("""
        <style>
            /* Define the CSS for our news card */
            .news-card {
                background-color: #f8f9fa; /* A light grey background */
                border: 1px solid #e9ecef; /* A subtle border */
                border-radius: 10px;      /* Rounded corners */
                padding: 15px;            /* Some space inside the card */
                margin-bottom: 20px;      /* Space between cards in the same column */
                box-shadow: 0 4px 8px 0 rgba(0,0,0,0.1); /* The shadow effect */
                height: 250px; /* Give a fixed height to align the cards */
                overflow-y: auto; /* Add a scrollbar if content overflows */
            }
            .news-card a {
                text-decoration: none; /* Remove underline from links */
                color: #007bff !important; /* A nice blue for the link */
                font-weight: bold;
            }
            .news-card .tags {
                margin-top: 10px; /* Space between title and tags */
            }
            .news-card .tag {
                background-color: #e9ecef;
                color: #495057;
                padding: 2px 8px;
                border-radius: 5px;
                font-size: 0.8em;
                margin-right: 5px;
            }
        </style>
    """, unsafe_allow_html=True)

# ==============================================================================
# Page Configuration & Data Loading
# ==============================================================================
st.set_page_config(layout="wide", page_title="AI Risk Hotspots Dashboard")

@st.cache_data
def load_data(filepath):
    """Loads and caches the final JSON data file."""
    with open(filepath, 'r') as f:
        data = json.load(f)
    return data

# ==============================================================================
# Main App Execution
# ==============================================================================
def main():
    """Main function to run the Streamlit app."""
    
    # Display the header section
    display_header_and_about()
    
    # Load the data once
    app_data = load_data('data/final_outputs.json')
    
    # Display each module by calling its respective function in order
    display_risk_radar(app_data)
    display_cause_effect_correlator(app_data)
    selected_category = display_dynamic_forecaster(app_data)

    news_placeholder = st.empty()

    display_key_insights(app_data)

    if selected_category:
        with news_placeholder.container():
             display_on_the_radar(selected_category)

if __name__ == "__main__":
    main()