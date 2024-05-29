import pandas as pd
import datetime as dt
import random
import smtplib

PASSWORD = "[Enter Your App Password]"
MY_EMAIL = "shubhyadav753@gmail.com"


# Read the csv
birthday_csv = pd.read_csv("100 Days code/Day 32 Birthday wisher/Birthday Automation/birthdays.csv")
data = birthday_csv.to_dict(orient="records")

#choose random file 
letter1="100 Days code/Day 32 Birthday wisher/Birthday Automation/letter_templates/letter_1.txt"
letter2="100 Days code/Day 32 Birthday wisher/Birthday Automation/letter_templates/letter_2.txt"
letter3="100 Days code/Day 32 Birthday wisher/Birthday Automation/letter_templates/letter_3.txt"
random_letter = random.choice([letter1, letter2, letter3])


# Working with datetime
now = dt.datetime.now()
for info in range(len(data)):
    if data[info]["month"] == now.month and data[info]["day"]==now.day:
        with open(random_letter, "r") as content:
            b_data = content.read()
            new_data = b_data.replace("[NAME]", data[info]["name"])
        
        # Sending the email to the person's email address
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls() 
            connection.login(user = MY_EMAIL, password = PASSWORD) 
            connection.sendmail(
                from_addr = MY_EMAIL, 
                to_addrs = data[info]["email"],
                msg=f"Subject:Happiest Birthday\n\n{new_data}")
            print("Msg Sent Successfully...")



