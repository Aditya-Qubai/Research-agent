import feedparser


AI_FEEDS = [
    "https://feeds.feedburner.com/oreilly/radar",
    "https://rss.arxiv.org/rss/cs.AI",
]


def fetch_ai_feeds():

    collected_articles = []

    for url in AI_FEEDS:

        feed = feedparser.parse(url)

        for entry in feed.entries[:5]:

            collected_articles.append({
                "title": entry.get("title", ""),
                "summary": entry.get("summary", ""),
                "link": entry.get("link", "")
            })

    return collected_articles