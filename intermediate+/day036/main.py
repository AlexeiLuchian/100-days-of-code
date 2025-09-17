import os
import requests
import datetime as dt
import twilio.rest
from info import twilio_sid, twilio_token, pn, tpn

STOCK = "NVDA"
COMPANY_NAME = "NVIDIA Corporation"
api_key = os.environ.get("ALPHAVANTAGE_API_KEY")
news_api_key = os.environ.get("NEWS_API_KEY")

alphavantage_endpoint = "https://www.alphavantage.co/query?"
av_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": api_key,
}

response = requests.get(url=alphavantage_endpoint, params=av_params)
response.raise_for_status()

data = response.json()

today = dt.date.today()
yesterday = today - dt.timedelta(days=1)
tdb_yesterday = today - dt.timedelta(days=2)

yesterday_str = yesterday.strftime('%Y-%m-%d')
tdb_yesterday_str = tdb_yesterday.strftime('%Y-%m-%d')

yesterday_close = data["Time Series (Daily)"][yesterday_str]["4. close"]
tdb_yesterday_close = data["Time Series (Daily)"][tdb_yesterday_str]["4. close"]

percentage = round(100 - float(yesterday_close) * 100 / float(tdb_yesterday_close), 2)

if True:
# if abs(percentage) > 5:
    if percentage > 0:
        emoji = "🔺"
    else:
        emoji = "🔻"
    news_endpoint = "https://newsapi.org/v2/everything?"
    news_params = {
    "q": COMPANY_NAME,
    "from": tdb_yesterday_str,
    "sortBy": "popularity",
    "apiKey": news_api_key,
    }

    news_response = requests.get(url=news_endpoint, params=news_params)
    news_response.raise_for_status()

    news_data = news_response.json()
    most_popular_articles = news_data["articles"][:3]
    messages = [f"Headline: {article['title']}\nBrief: {article['description']}" for article in most_popular_articles]

    client = twilio.rest.Client(twilio_sid, twilio_token)
    for message in messages:
        client.messages.create(body=f"{STOCK}: {emoji}{percentage}%\n{message}", from_=tpn, to=pn)