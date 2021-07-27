##################### Extra Hard Starting Project ######################
import pandas
import datetime as dt
import random
import smtplib
import os

EMAIL = os.environ.get("EMAIL_ADDRESS")
PASSWORD = os.environ.get("PASSWORD")
SMTP = os.environ.get("SMTP")

LETTERLIST = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
# 1. Update the birthdays.csv
data_cumpleanos = pandas.read_csv("birthdays.csv")
dict_cumpleanos = data_cumpleanos.to_dict(orient="records")
# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()

for person in dict_cumpleanos:
    if now.month == int(person["month"]) and now.day == int(person["day"]):
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
        letter_selection = random.choice(LETTERLIST)
        with open("./letter_templates/"+letter_selection, mode="r") as file_letter:
            letter = file_letter.read()
        letter = letter.replace("[NAME]", person["name"])
# 4. Send the letter generated in step 3 to that person's email address.
        with smtplib.SMTP(SMTP) as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=EMAIL, to_addrs=person["email"], msg="Subject:Happy Birthday\n\n"+letter)



