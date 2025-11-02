# ui_components/module_4_insights.py
import streamlit as st
from textwrap import dedent

def display_key_insights(data):
    """Displays the final summary of Key Insights & Takeaways."""
    st.header("Key Insights & Takeaways")
    
    sorted_forecasts_array = data.get('all_forecasts_data', [])

    if sorted_forecasts_array:
        top_hotspot = sorted_forecasts_array[0]['category_name']
        flatter_category = sorted_forecasts_array[-1]['category_name']
        
        insight_text = dedent(f"""
            Based on the data and forecasts presented in this dashboard, we can draw several key conclusions:

            1.  **The Top Warning:** Our system identifies **"{top_hotspot}"** as the #1 accelerating risk category. The forecast projects a significant increase in these incidents, indicating an urgent need for prioritized research into targeted mitigation strategies.

            2.  **The Macro Trend is Clear:** There is a strong visual correlation between the exponential growth in AI training compute (the "Cause") and the overall rising number of real-world AI incidents across all categories (the "Effect").

            3.  **Not All Risks Behave Alike:** The forecaster reveals that different harm categories have different trajectories. While **"{top_hotspot}"** is a clear, accelerating hotspot, other categories like **"{flatter_category}"** represent more chronic, persistent problems, requiring different safety strategies.
        """)
    else:
        insight_text = dedent("""
            Based on the data presented in this dashboard, we can draw several key conclusions:

            *   **The Macro Trend is Clear:** There is a strong visual correlation between the exponential growth in AI training compute (the "Cause") and the overall rising number of real-world AI incidents across all categories (the "Effect").

            *   **Further Analysis Needed:** The forecasting module requires sufficient data to identify specific risk hotspots and their individual trajectories.
        """)

    st.markdown(insight_text)