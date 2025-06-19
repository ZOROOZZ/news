import os, json, random
from datetime import datetime
import yfinance as yf

os.makedirs("static/data", exist_ok=True)

# Companies to track with ticker symbols
companies = {
    "Tata Motors": "TTM",
    "Adani Ports": "ADNT",
    "Infosys": "INFY",
    "Wipro": "WIT",
    "Reliance": "RELI"
}

headlines = []

for name, ticker in companies.items():
    stock = yf.Ticker(ticker)
    hist = stock.history(period="2d")
    if len(hist) < 2:
        continue
    pct_change = ((hist["Close"][-1] - hist["Close"][-2]) / hist["Close"][-2]) * 100

    if pct_change > 3:
        headlines.append({"title": f"{name} shares soar {pct_change:.2f}% on strong market performance", "source": "ZORO AI", "time": datetime.now().isoformat()})
    elif pct_change < -3:
        headlines.append({"title": f"{name} shares plunge {pct_change:.2f}% amid market sell‑off", "source": "ZORO AI", "time": datetime.now().isoformat()})
    else:
        headlines.append({"title": f"{name} remains steady ({pct_change:+.2f}%) in recent trading", "source": "ZORO AI", "time": datetime.now().isoformat()})

# Fill remaining slots with template headlines
actions = ["announces merger deal", "faces regulatory pipeline delays", "launches new product line"]
while len(headlines) < 10:
    comp = random.choice(list(companies.keys()))
    headlines.append({"title": f"{comp} {random.choice(actions)}", "source": "ZORO AI", "time": datetime.now().isoformat()})

output = {"updated": datetime.now().isoformat(), "headlines": headlines[:10]}

with open("static/data/news.json", "w", encoding="utf-8") as f:
    json.dump(output, f, indent=2)
