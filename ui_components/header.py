# ui_components/header.py
import streamlit as st
from textwrap import dedent 

def display_header_and_about():
    """Displays the main title, intro, and the 'About' expander."""
    st.title("🚨 AI Risk Hotspots: Early Warning System")
    st.markdown(dedent("""
        This dashboard provides a data-driven overview of the AI harm landscape, correlating real-world incidents with the growth in AI capabilities.
        It serves as an early warning system to identify and forecast emerging risk categories.
    """)) 
    
    with st.expander("ℹ️ About This Project & Data Sources"):
        st.markdown(dedent("""
            **Mission:** This dashboard is an open-source Situational Awareness System for AI risk. Created for the AI Forecasting Hackathon 2025, it provides a data-driven view of the historical harm landscape and serves as an early warning system by forecasting emerging risk hotspots.
            
            ---
            
            #### Data Sources
            
            **1. The "Effect" Data (AI Incidents):**
            *   Incident data is sourced from the **AI Incident Database**.
            *   **Link:** [incidentdatabase.ai](https://incidentdatabase.ai/)
            
            **2. The "Cause" Data (AI Capability Growth):**
            *   Historical AI capability growth is measured using **Training Compute (measured in FLOPs)** from **Epoch AI**. (A FLOP is a basic unit of computation, representing the total computational work invested in training a model).
            *   We specifically use the **"Notable AI Models"** dataset from the `Data on AI Models` category.
            *   **Link:** [epoch.ai/data/ai-models](https://epoch.ai/data/ai-models)
        """)) 