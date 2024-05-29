import smtplib
import datetime as dt
import random

PASSWORD = "[Enter Your App Password]"
MY_EMAIL = "shubhyadav753@gmail.com"

    
now = dt.datetime.now()
weekday = now.weekday()
if weekday == 2:

    with open("100 Days code/Day 32 Birthday wisher/quotes.txt") as quotes:
        lines = quotes.readlines() # Read the file and split it into a list of lines where each line is a string that contains one or more sentences
        choose_line = random.choice(lines)
        print(choose_line)
    
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls() #Transport Layer Security
        connection.login(user = MY_EMAIL, password = PASSWORD) #Login to the email account using a secure connection (TLS/SSL).
        connection.sendmail(
            from_addr = MY_EMAIL, 
            to_addrs = "shubhyadav4838@gmail.com",
            msg=f"Subject:Monday Motivation\n\n{choose_line}")
