import feedparser
import json

# Your 5 favorite news links
FEEDS = [
    "https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml",
    "https://feeds.bbci.co.uk/news/rss.xml",
    # Add 3 more here!
]

all_news = []

for url in FEEDS:
    feed = feedparser.parse(url)
    # Grab only the top 3 stories
    for entry in feed.entries[:3]:
        img = entry.get('media_content', [{}])[0].get('url', 'https://via.placeholder.com/400')
        all_news.append({
            "title": entry.title,
            "image": img,
            "link": entry.link
        })

# Save it to a file the website can read
with open('news.json', 'w') as f:
    json.dump(all_news, f)
