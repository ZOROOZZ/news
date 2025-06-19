import os
import requests
import json
from datetime import datetime

# Create the directory if it doesn't exist
os.makedirs("static/data", exist_ok=True)

API_KEY = os.getenv("NEWS_API_KEY")
URL = f"https://newsapi.org/v2/top-headlines?country=in&category=business&pageSize=10&apiKey={API_KEY}"

res = requests.get(URL)
news_data = res.json()

# Print API response for debug
print("API RESPONSE:", json.dumps(news_data, indent=2))

if "articles" not in news_data:
    raise Exception(f"News API error: {news_data.get('message', 'Unknown error')}")

headlines = [
    {
        "title": item["title"],
        "source": item["source"]["name"],
        "time": item["publishedAt"]
    }
    for item in news_data["articles"]
]

output = {
    "updated": datetime.now().isoformat(),
    "headlines": headlines
}

with open("static/data/news.json", "w", encoding="utf-8") as f:
    json.dump(output, f, indent=2)
