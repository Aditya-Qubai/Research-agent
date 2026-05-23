from services.rss_ingestion import fetch_ai_feeds
from database.intelligence_memory import store_intelligence


def ingest_rss_intelligence():

    articles = fetch_ai_feeds()

    combined_text = ""

    for article in articles:

       store_intelligence(
        article["title"],
        article["summary"]
       )

       combined_text += f"""

       TITLE:
       {article['title']}

       SUMMARY:
       {article['summary']}

       """