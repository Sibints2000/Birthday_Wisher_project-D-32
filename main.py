import smtplib

my_email = "thurrappattujoseph@gmail.com"
password = "thurrappattu@007"

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email, password=password)
