import streamlit as st
import pandas as pd
import plotly.graph_objects as go

def display_cause_effect_correlator(data):
    """Displays Module 2: The Cause & Effect Correlator."""
    st.header("Module 2: The Cause & Effect Correlator")
    st.markdown("This chart visualizes our core thesis: as the **Cause** (total training compute for notable AI models) grows exponentially, the **Effect** (the number of real-world AI incidents) rises with it.")

    df_cause_effect = pd.DataFrame(data['cause_effect_data'])
    fig_cause_effect = go.Figure()
    fig_cause_effect.add_trace(go.Bar(x=df_cause_effect['year'], y=df_cause_effect['incident_count'], name='Number of Incidents', marker_color='indianred'))
    fig_cause_effect.add_trace(go.Scatter(x=df_cause_effect['year'], y=df_cause_effect['total_compute_flops'], name='Training Compute (FLOPs)', yaxis='y2', mode='lines+markers', line=dict(color='royalblue', width=3)))
    fig_cause_effect.update_layout(
        title_text="Incident Count vs. AI Training Compute Over Time", xaxis_title="Year",
        yaxis=dict(title="Number of Incidents"),
        yaxis2=dict(title="Total Training Compute (FLOPs) - Log Scale", overlaying="y", side="right", type="log"),
        legend=dict(x=0.01, y=0.99), height=500
    )
    st.plotly_chart(fig_cause_effect, use_container_width=True)