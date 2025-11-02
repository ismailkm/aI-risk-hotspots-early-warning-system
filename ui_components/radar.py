import streamlit as st
import pandas as pd
import plotly.express as px
from constants import CATEGORY_DEFINITIONS

def display_risk_radar(data):
    """Displays Module 1: The Risk Radar and its definitions expander."""
    st.header("Module 1: The Risk Radar")
    st.markdown("This visualization tracks the number of AI incidents over time, broken down by their primary harm category. It helps identify which types of risks are becoming more prevalent.")

    df_risk_radar = pd.DataFrame(data['risk_radar_data'])
    df_risk_radar['quarter_str'] = pd.to_datetime(df_risk_radar['quarter_str'])

    all_categories = sorted(df_risk_radar['harm_category'].unique())
    selected_categories = st.multiselect(
        'Select harm categories to display:', options=all_categories, default=all_categories
    )

    if selected_categories:
        df_filtered = df_risk_radar[df_risk_radar['harm_category'].isin(selected_categories)]
        fig_risk_radar = px.area(
            df_filtered, x='quarter_str', y='incident_count', color='harm_category',
            title="AI Incidents by Harm Category Over Time",
            labels={'quarter_str': 'Quarter', 'incident_count': 'Number of Incidents'}, height=500
        )
        st.plotly_chart(fig_risk_radar, use_container_width=True)
    else:
        st.warning("Please select at least one harm category.")

    with st.expander("📖 What do the harm categories mean?"):
        st.markdown("These nine categories group AI incidents based on the primary root cause of the harm.")
        for category, definition in CATEGORY_DEFINITIONS.items():
            st.markdown(f"*   **{category}:** {definition}")