import feedparser
import json
import os

# Your 5 selected news links
FEEDS = [
    "https://growcola.com/feed/",             # Growcola
    "https://news.yahoo.com/rss/",            # Yahoo News
    "https://rss.dw.com/xml/rss-en-all",      # DW All (English version for variety)
    "https://www.leafly.com/feed"             # Leafly
]

all_news = []

for url in FEEDS:
    try:
        feed = feedparser.parse(url)
        # Grab only the top 5 stories from each feed
        for entry in feed.entries[:5]:
            # This looks for the best image available
            img_url = "https://via.placeholder.com/800x450?text=No+Image+Available"
            
            # 1. Check for media content (common in Yahoo/DW)
            if 'media_content' in entry and len(entry.media_content) > 0:
                img_url = entry.media_content[0]['url']
            # 2. Check for enclosures (common in Growcola/Leafly)
            elif 'links' in entry:
                for link in entry.links:
                    if 'image' in link.get('type', ''):
                        img_url = link.get('href')
            
            all_news.append({
                "source": feed.feed.get('title', 'News Source'),
                "title": entry.title,
                "image": img_url,
                "link": entry.link,
                "summary": entry.get('summary', '')[:150] + "..." # Short snippet
            })
    except Exception as e:
        print(f"Error reading {url}: {e}")

# Save the news to a file that our website can read
with open('news.json', 'w') as f:
    json.dump(all_news, f, indent=4)
