from services.rss_ingestion import fetch_ai_feeds


def ingest_rss_intelligence():

    articles = fetch_ai_feeds()

    combined_text = ""

    for article in articles:

        combined_text += f"""
        
        TITLE:
        {article['title']}
        
        SUMMARY:
        {article['summary']}
        
        """

    return combined_text