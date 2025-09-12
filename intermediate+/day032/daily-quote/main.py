import smtplib
import datetime as dt
from random import choice
from info import from_email, password

to_email = from_email

today = dt.datetime.now()
day_of_week = today.weekday()

if day_of_week == 0:
    with open("quotes.txt") as file:
        quotes = file.readlines()
        quote = choice(quotes)

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=from_email, password=password)
        connection.sendmail(from_addr=from_email,
                            to_addrs=to_email, 
                            msg=f"Subject:Monday Quote\n\n{quote}")