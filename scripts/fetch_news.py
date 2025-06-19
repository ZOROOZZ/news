import os
import json
import random
from datetime import datetime

os.makedirs("static/data", exist_ok=True)

companies = ["Reliance", "Tata Motors", "Infosys", "Wipro", "Adani Ports", "HDFC Bank", "Zomato"]
actions = [
    "shares soar after quarterly earnings", "under scrutiny amid market volatility",
    "announces new merger deal", "launches green energy initiative",
    "faces regulatory investigation", "expands into international markets"
]

headlines = [
    {
        "title": f"{random.choice(companies)} {random.choice(actions)}",
        "source": "ZORO AI",
        "time": datetime.now().isoformat()
    }
    for _ in range(10)
]

output = {
    "updated": datetime.now().isoformat(),
    "headlines": headlines
}

with open("static/data/news.json", "w", encoding="utf-8") as f:
    json.dump(output, f, indent=2)
