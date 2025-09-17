import os
import requests
import datetime as dt

STOCK = "NVDA"
COMPANY_NAME = "NVIDIA Corporation"
api_key = os.environ.get("ALPHAVANTAGE_API_KEY")

alphavantage_endpoint = "https://www.alphavantage.co/query?"
params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": api_key,
}

response = requests.get(url=alphavantage_endpoint, params=params)
response.raise_for_status()

data = response.json()

today = dt.date.today()
yesterday = today - dt.timedelta(days=1)
tdb_yesterday = today - dt.timedelta(days=2)

yesterday_str = yesterday.strftime('%Y-%m-%d')
tdb_yesterday_str = tdb_yesterday.strftime('%Y-%m-%d')

yesterday_close = data["Time Series (Daily)"][yesterday_str]["4. close"]
tdb_yesterday_close = data["Time Series (Daily)"][tdb_yesterday_str]["4. close"]

five_pct = float(tdb_yesterday_close) * 0.05

print(five_pct)
print(yesterday_close)
print(tdb_yesterday_close)

if float(yesterday_close) > float(tdb_yesterday_close) + five_pct or float(yesterday_close) < float(tdb_yesterday_close) - five_pct:
    print("Get News!")

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

