import requests
from bs4 import BeautifulSoup
import json
import os
from datetime import datetime

# Create output folder
os.makedirs("static/data", exist_ok=True)

# Scrape MoneyControl business news
url = "https://www.moneycontrol.com/news/business/"
headers = {"User-Agent": "Mozilla/5.0"}
res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.content, "html.parser")

# Extract headlines
headlines = []
for item in soup.select("li.clearfix > a"):
    title = item.get_text(strip=True)
    if title:
        headlines.append({
            "title": title,
            "source": "Moneycontrol",
            "time": datetime.now().isoformat()
        })

# Save the first 10
output = {
    "updated": datetime.now().isoformat(),
    "headlines": headlines[:10]
}

with open("static/data/news.json", "w", encoding="utf-8") as f:
    json.dump(output, f, indent=2)
