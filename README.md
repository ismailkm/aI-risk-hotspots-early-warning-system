# 🚨 AI Risk Hotspots: An Early Warning System

> A data-driven **Situational Awareness System** for AI risk. This dashboard tracks real-world AI incidents, correlates them with growing AI capabilities, and forecasts emerging "hotspots" to inform AI safety and governance.
>
> *Project for the Apart Research AI Forecasting Hackathon 2025.*

---

## 🚀 Key Features & Insights

Our interactive dashboard, built with Streamlit, provides a multi-layered view of the AI harm landscape:

*   **📈 Module 1: The Risk Radar:** A historical overview of AI incidents, showing a dramatic acceleration in the frequency and variety of harms since 2020.

*   **🔗 Module 2: The Cause & Effect Correlator:** A powerful visualization proving our core thesis: as AI training compute grows exponentially, the number of real-world incidents rises with it.

*   **🔮 Module 3: The Dynamic Forecaster:** An early warning tool that identifies the fastest-accelerating harm categories and projects their 3-year trajectory. Our analysis identifies **"Malicious Use & Security"** as the #1 current hotspot.

*   **📡 Module 4: On the Radar:** An automated research assistant that fetches and ranks the latest news related to a selected harm category, providing real-time, real-world context for the data trends.

---

## 🛠️ How to Run Locally

This project is containerized using Docker for a simple, one-command setup.

**Prerequisites:**
*   Docker & Docker Compose

**Steps:**

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/your-username/ai-risk-dashboard.git
    cd ai-risk-dashboard
    ```

2.  **Run with Docker Compose:**
    This single command builds the Docker image and starts the Streamlit application.
    ```bash
    docker-compose up
    ```

3.  **View the Dashboard:**
    Open your web browser and navigate to **`http://localhost:8501`**.

---

## 📊 Data Sources

*   **Incident Data:** Sourced from the **AI Incident Database**. The raw data can be downloaded from their [research snapshots page](https://incidentdatabase.ai/research/snapshots/).
*   **Compute Data:** Sourced from **Epoch AI**. We use the ["Notable AI Models"](https://epoch.ai/data/ai-models) dataset from the "Data on AI Models" category.

---

## 🏗️ Project Structure & Methodology

The project is structured into a data processing pipeline and the final dashboard application.

### Data Processing Pipeline (`/notebooks/`)

The notebooks in this folder document the step-by-step process of transforming raw data into the final `final_outputs.json` file used by the dashboard. They are numbered in execution order and provide full transparency into our methodology.

1.  `merge-ai-incidents-dataset.ipynb`
2.  `manual-classification.ipynb`
3.  `ai-incident-llm-classification.ipynb`
4.  `cleaning-epoch-ai-data.ipynb`
5.  `analysis-prep-visualizations.ipynb`
6.  `hotspot-micro-analysis.ipynb`

### Dashboard Application

*   `/dashboard.py`: The main Streamlit script that orchestrates the UI.
*   `/ui_components/`: A package containing all modular UI components.
*   `/data/final_outputs.json`: The final processed data file that powers the dashboard.
*   `Dockerfile` & `docker-compose.yml`: Configuration for the containerized environment.

---

## 💡 Future Work

*   **Formal Validation:** Implement a script to formally validate the LLM classifier's accuracy against our "gold standard" set.
*   **Advanced Forecasting:** Explore more sophisticated time-series models (e.g., ARIMA) to capture more complex, non-linear trends.
*   **Automated Micro-Analysis:** Integrate a second LLM to automate the thematic analysis of hotspots, turning the final "Recommendations" section into a dynamic feature.