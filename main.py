import smtplib
import datetime as dt
from random import choice

date=dt.datetime.now()
weekday=date.weekday()


if weekday==0 or 1 or 2 or 3 or 4 or 5 or 6: #monday starts with 0
    with open("quotes.txt") as data:
        quote=data.readlines()
        random_quote=choice(quote)
        print(random_quote)

    EMAIL= "deepam@gmail.com"      #use your own email
    # first go to your google account and generate app password for python  #
    PASSWORD="deepam"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=EMAIL,password=PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=EMAIL,
            msg=f"Subject:Daily Quote\n\n{random_quote}"
        )