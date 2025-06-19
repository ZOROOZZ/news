import requests
from bs4 import BeautifulSoup
import json
import os
from datetime import datetime

os.makedirs("static/data", exist_ok=True)

url = "https://www.moneycontrol.com/news/business/"
res = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})

soup = BeautifulSoup(res.content, "html.parser")

headlines = []
for item in soup.select("li.clearfix > a"):
    title = item.get_text(strip=True)
    if title:
        headlines.append({
            "title": title,
            "source": "Moneycontrol",
            "time": datetime.now().isoformat()
        })

output = {
    "updated": datetime.now().isoformat(),
    "headlines": headlines[:10]
}

with open("static/data/news.json", "w", encoding="utf-8") as f:
    json.dump(output, f, indent=2)
