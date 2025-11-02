# ui_components/module_3a_on_the_radar.py
import streamlit as st
import pandas as pd
import requests
import json
from datetime import date, timedelta
from textwrap import dedent

from constants import CATEGORY_KEYWORDS

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
                min-height: 150px; /* Give a fixed height to align the cards */
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
# Helper Function to Fetch News
# ==============================================================================
def fetch_latest_news(days_to_fetch=30):
    """Fetches the last N days of news from the AIID GraphQL API."""
    # ... (This is the complete, robust fetch_latest_news function from before)
    print(f"--- FETCHING LATEST NEWS for the last {days_to_fetch} days ---")
    
    url = "https://incidentdatabase.ai/api/graphql"
    headers = {'Content-Type': 'application/json'}

    end_date = date.today()
    start_date = end_date - timedelta(days=days_to_fetch)
    
    list_of_date_strings = []
    current_date = start_date
    while current_date <= end_date:
        list_of_date_strings.append(current_date.strftime('%Y-%m-%d'))
        current_date += timedelta(days=1)

    chunk_size = 15
    all_candidates = []
    retries = 2

    for i in range(0, len(list_of_date_strings), chunk_size):
        chunk_dates = list_of_date_strings[i:i + chunk_size]
        payload = { "operationName": "NewsArticles", "variables": {"filter": {"match": {"EQ": True}, "date_published": {"IN": chunk_dates}}}, "query": "query NewsArticles($filter: CandidateFilterType!) {\n  candidates(filter: $filter) {\n    title\n    url\n    date_published\n    text\n    similarity\n    matching_harm_keywords\n  }\n}" }

        for attempt in range(retries):
            try:
                response = requests.post(url, headers=headers, data=json.dumps(payload), timeout=30)
                if response.status_code == 200:
                    all_candidates.extend(response.json().get('data', {}).get('candidates', []))
                    break 
            except requests.exceptions.RequestException:
                pass
    return all_candidates

# ==============================================================================
# Main Display Function for this Component
# ==============================================================================
def display_on_the_radar(selected_category):
    """Displays the 'On the Radar' expander and its content for a given category."""

    inject_custom_css()

    with st.expander(f"📡 On the Radar: See Latest Events for '{selected_category}'"):
        with st.spinner("Fetching and analyzing the latest news..."):
            articles = fetch_latest_news()

            if not articles:
                st.warning("Could not fetch the latest news at this time. Please try again later.")
                return

            df_articles = pd.DataFrame(articles)
            keywords = CATEGORY_KEYWORDS.get(selected_category, [])

            if not keywords:
                st.info("No specific keywords are defined for this category to filter news.")
                return

            def calculate_relevance(row):
                score = 0
                text_to_search = f"{row.get('title', '')} {row.get('text', '')}".lower()
                for keyword in keywords:
                    if keyword in text_to_search:
                        score += 1
                if isinstance(row.get('matching_harm_keywords'), list):
                    for harm_keyword in row['matching_harm_keywords']:
                        if harm_keyword in keywords:
                            score += 2
                return score

            df_articles['relevance_score'] = df_articles.apply(calculate_relevance, axis=1)
            df_relevant = df_articles[df_articles['relevance_score'] > 0].sort_values(by=['relevance_score', 'similarity'], ascending=False)

            if df_relevant.empty:
                st.info(f"No recent news articles matching the keywords for **{selected_category}** were found.")
                return

            num_cols = 3
            # We will show a maximum of 9 articles.
            top_articles = df_relevant.head(9)
            
            # Round down to the nearest multiple of 3 to ensure full rows
            num_to_show = (len(top_articles) // num_cols) * num_cols

            if num_to_show == 0:
                st.info(f"Found {len(top_articles)} relevant articles, but not enough to form a full row.")
                return
                
            st.success(f"Found {len(df_relevant)} relevant articles. Displaying the Top {num_to_show}.")

            # --- Prepare rows of columns ---
            # This loop will run once for each row of cards (e.g., for 6 articles, it runs twice)
            for i in range(0, num_to_show, num_cols):
                # Create a new set of columns for each row
                cols = st.columns(num_cols)
                
                # Get the 3 articles for the current row
                row_articles = top_articles.iloc[i : i + num_cols]
                
                # Place each of the 3 articles into a column
                for j, row in enumerate(row_articles.itertuples()):
                    with cols[j]:
                        date_obj = pd.to_datetime(row.date_published)
                        formatted_date = date_obj.strftime('%d-%m-%Y')
                        tags_html = "".join([f"<span class='tag'>{tag}</span>" for tag in (row.matching_harm_keywords or [])])
                        
                        card_html = f"""
                            <div class="news-card">
                                <a href="{row.url}" target="_blank">{row.title}</a>
                                <p style="font-size: 0.9em; color: grey; margin-top: 10px;">Published: {formatted_date}</p>
                                <div class="tags">{tags_html}</div>
                            </div>
                        """
                        st.markdown(card_html, unsafe_allow_html=True)
            
            st.markdown("---")
            st.info(dedent("""
                **Next Steps:**
                
                1.  **Review the articles above.** If you find a relevant research paper mentioned, note its title.
                2.  **Find the primary source** by searching for the paper's title on **[arXiv.org](https://arxiv.org/)**.
                
                *News sourced from the AI Incident Database News Digest. [Click here to view the full, live feed.](https://incidentdatabase.ai/apps/newsdigest/)*
            """))

  