from datetime import datetime
import re


def get_days_from_today(date):
    today = datetime.today().date()
    new_day = date - today
    return new_day.days

while True:
    try:
        inp_date = input("Print your date: ")
        def correct_date (date_str):
            date = re.match(r"(\d{2})-(\d{2})-(\d{4})", date_str)
            if date == True:
                return f"{date.group(3)}-{date.group(1)}-{date.group(2)}"
            else:
                date = re.match(r"(\d{2})-(\d{1})-(\d{4})", date_str)
                return f"{date.group(3)}-{date.group(1)}-{date.group(2)}"
            return date_str

        reforming_date = re.sub(r"[./\s\\]", "-", inp_date)
        new_date = correct_date(reforming_date)
        date = datetime.strptime(new_date, "%Y-%m-%d").date()
        break
    except ValueError:
        print("Incorrect input, try again!")

get_days_from_today(date)