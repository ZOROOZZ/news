import requests
from bs4 import BeautifulSoup
import json

url = "https://www.moneycontrol.com/news/business/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

# Moneycontrol often uses this structure for news listings
articles = soup.select("ul#cagetory-news-list li.clearfix")

headlines = []
for article in articles[:10]:  # Limit to 10 articles
    try:
        headline = article.select_one("h2 a").get_text(strip=True)
        link = article.select_one("a")["href"]
        time = article.select_one("span.datetime").get_text(strip=True)
        
        headlines.append({
            "title": headline,
            "link": link if link.startswith("http") else f"https://www.moneycontrol.com{link}",
            "time": time
        })
    except AttributeError:
        continue

print(json.dumps(headlines, indent=2))
