import smtplib
import datetime as dt
import random

MY_EMAIL = "thurrappattujoseph@gmail.com"
MY_PASSWORD = "thurrappattu@007"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 4:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Monday Motivation\n\n{quote}"
        )




import smtplib

my_email = "thurrappattujoseph@gmail.com"
password = "thurrappattu@007"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="sibin321@yahoo.com",
        msg="Subject:Hello\n\nThis is the bod of my email"
    )
