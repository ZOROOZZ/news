import os
import requests
import json
from datetime import datetime

API_KEY = os.getenv("NEWS_API_KEY")
URL = "https://newsapi.org/v2/top-headlines?country=in&category=business&pageSize=10&apiKey=" + API_KEY

res = requests.get(URL)
news_data = res.json()

headlines = [
    {
        "title": item["title"],
        "source": item["source"]["name"],
        "time": item["publishedAt"]
    }
    for item in news_data.get("articles", [])
]

output = {
    "updated": datetime.now().isoformat(),
    "headlines": headlines
}

with open("data/news.json", "w", encoding="utf-8") as f:
    json.dump(output, f, indent=2)
