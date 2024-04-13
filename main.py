##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv
# 2. Check if today matches a birthday in the birthdays.csv
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# 4. Send the letter generated in step 3 to that person's email address.

import random as rd
import datetime as dt
import smtplib
import pandas as pd
# import csv


def send_email(email, subject, content):
    email_from = ""
    password = ""

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=email_from, password=password)
        connection.sendmail(
            from_addr=email_from,
            to_addrs=email,
            msg=f"Subject:{subject}\n\n{content}")


def get_today():
    return dt.datetime.now().day, dt.datetime.now().month


def get_random_letter():
    file_name = f"./letter_templates/letter_{rd.randint(1, 3)}.txt"
    with open(file_name) as file:
        return file.read()


def main():
    data = pd.read_csv("birthdays.csv")
    birthdays = {(data_row["day"], data_row["month"]): data_row for (index, data_row) in data.iterrows()}

    if get_today() in birthdays:
        person = birthdays[get_today()]
        email = person["email"]
        subject = f"Happy birthday {person['name']}"
        content = get_random_letter().replace("[NAME]", person["name"])

        print(email, subject)
        print(content)
        # send_email(email, subject, content)


main()

# OLD VERSION
# def is_today_birthday(day, month):
#     today = (dt.datetime.now().day, dt.datetime.now().month)
#     return day == today[0] and month == today[1]
# with open("birthdays.csv", newline='') as birthdays_file:
#     reader = csv.reader(birthdays_file)
#     lines = [row for index, row in enumerate(reader) if index != 0]
#     people = []
#     for index, row in enumerate(reader):
#         if index > 0:
#             people.append({
#                 "name": row[0],
#                 "email": row[1],
#                 "year": int(row[2]),
#                 "month": int(row[3]),
#                 "day": int(row[4])
#             })
#
#     for person in people:
#         if is_today_birthday(person["day"], person["month"]):
#             email = person["email"]
#             subject = f"Happy birthday {person['name']}"
#             content = get_random_letter().replace("[NAME]", person["name"])
#
#             # send_email(email, subject, content)
