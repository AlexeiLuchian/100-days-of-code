import datetime as dt
import pandas
import smtplib
from random import randint
from info import from_email, password

# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
date = now.day
month = now.month

dataframe = pandas.read_csv("birthdays.csv")
possible_birthdays = dataframe[dataframe["day"] == date]
certain_birthdays = possible_birthdays[possible_birthdays["month"] == month]

names = {row["name"]:row["email"] for (index, row) in certain_birthdays.iterrows()}
for name in names:
    email = names[name]

    letter_number = randint(1, 3)
    with open(f"letter_templates/letter_{letter_number}.txt") as file:
        message = file.readlines()
        message = ''. join(message)
        modified_msg = message.replace('[NAME]', name)

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=from_email, password=password)
        connection.sendmail(from_addr=from_email,
                            to_addrs=email,
                            msg=f"Subject:Happy Birthday!\n\n{modified_msg}")