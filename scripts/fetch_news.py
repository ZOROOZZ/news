import requests
from bs4 import BeautifulSoup
import json
import os
from datetime import datetime

# Ensure the output folder exists
os.makedirs("static/data", exist_ok=True)

# Scrape from Moneycontrol - Latest Business News
url = "https://www.moneycontrol.com/news/business/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

try:
    res = requests.get(url, headers=headers, timeout=10)
    res.raise_for_status()  # Check for HTTP errors
    soup = BeautifulSoup(res.content, "html.parser")
    
    headlines = []
    
    # More specific selector for Moneycontrol's news items
    for item in soup.select("li.clearfix"):
        title_element = item.select_one("h2 a")
        if title_element:
            title = title_element.get_text(strip=True)
            if title and len(title) > 10:  # Reasonable length filter
                link = title_element["href"]
                time_element = item.select_one(".datetime")
                time = time_element.get_text(strip=True) if time_element else datetime.now().strftime("%H:%M")
                
                headlines.append({
                    "title": title,
                    "link": link,
                    "source": "Moneycontrol",
                    "time": time,
                    "scraped_at": datetime.now().isoformat()
                })
    
    # Save only top 10
    output = {
        "updated": datetime.now().isoformat(),
        "count": len(headlines[:10]),
        "headlines": headlines[:10]
    }
    
    with open("static/data/news.json", "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Successfully scraped {len(headlines[:10])} headlines from Moneycontrol.")
    print(f"📰 Sample headline: {headlines[0]['title'] if headlines else 'N/A'}")

except requests.exceptions.RequestException as e:
    print(f"❌ Error fetching data: {e}")
except Exception as e:
    print(f"❌ An unexpected error occurred: {e}")
