import requests
from datetime import date, timedelta
from twilio.rest import Client

STOCK = ""
COMPANY_NAME = ""
API_KEY = ""
NEWS_API = ""

yesterday_date = date.today() - timedelta(days=1)
day_before_yesterday = date.today() - timedelta(days=2)

STOCK_PARAMETERS = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": API_KEY,
    "outputsize": "compact"
}
NEWS_PARAMETERS = {
    "q": STOCK,
    "from": yesterday_date,
    "sortBy": "popularity",
    "apiKey": NEWS_API
}

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

def check_status(day1, day2):
    if day1 > day2:
        more = day1 - day2
        percentage_change = (more / day2) * 100
        return ["I", round(percentage_change, 1)]
    elif day2 > day1:
        more = day2 - day1
        percentage_change = (more / day2) * 100
        return ["D", round(percentage_change, 1)]
    else:
        return ["NO"]

response = requests.get(url=STOCK_ENDPOINT, params=STOCK_PARAMETERS)
data = response.json()
yesterday_data = data["Time Series (Daily)"][str(yesterday_date)]['4. close']
day_before_data = data["Time Series (Daily)"][str(day_before_yesterday)]['4. close']
result_data = check_status(float(yesterday_data), float(day_before_data))

news_response = requests.get(url=NEWS_ENDPOINT, params=NEWS_PARAMETERS)
news_data = news_response.json()
news_headline = news_data["articles"][0]["title"]
news_description = news_data["articles"][0]["description"]

if result_data[0] == "I":
    conclusion = f"{COMPANY_NAME}:🔺{result_data[1]}% Increase in stock price."
elif result_data[0] == "D":
    conclusion = f"{COMPANY_NAME}:🔻{result_data[1]}% Decrease in stock price."
else:
    conclusion = "No change detected for the last 24 hours. Please check back later to see if there is any news about this company's stock prices."

print(conclusion)
print("Headline: ", news_headline)
print("Brief: ", news_description)

account_sid = ''
auth_token = ''

# just do the change and write the code of twilio

print("Message sent successfully!")
