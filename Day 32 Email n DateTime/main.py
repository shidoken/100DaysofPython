# import smtplib

# my_email = 'email'
# password = 'password'

# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email,
#                         to_addrs="email", 
#                         msg="Subject:hello\n\nThis is the body of my email."
#     )


# import datetime as dt

# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_the_week = now.weekday()

# if day_of_the_week == 1:
#     print(day_of_the_week)

# date_of_birth = dt.datetime(year=1995, month=12, day=6, hour=4)
# print(date_of_birth)



#  =========================================

import smtplib
import datetime as dt
import random

MY_EMAIL = "email"
MY_PASSWORD = "password"

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
            to_addrs="email",
            msg=f"Subject:Monday Motivation\n\n{quote}"
        )

