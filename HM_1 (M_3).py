from datetime import datetime
import re


def get_days_from_today(date_str):
    def correct_date(date_str):
        date = re.match(r"(\d{2})-(\d{2})-(\d{4})", date_str)
        if date:
            return f"{date.group(3)}-{date.group(2)}-{date.group(1)}"
        else:
            date = re.match(r"(\d{2})-(\d{1})-(\d{4})", date_str)
            return f"{date.group(3)}-{date.group(2)}-{date.group(1)}"
        return date_str

    try:
        reforming_date = re.sub(r"[./\s\\]", "-", date_str)
        date = datetime.strptime(reforming_date, "%Y-%m-%d").date()
    except:
        new_date = correct_date(reforming_date)
        date = datetime.strptime(new_date, "%Y-%m-%d").date()

    today = datetime.today().date()
    new_day = date - today
    return new_day.days

while True:
    inp_date = input("Print your date: ")
    try:
        days_difference = get_days_from_today(inp_date)
        print(f"Days from today: {days_difference}")
        break
    except ValueError:
        print("Incorrect input, try again!")

get_days_from_today(inp_date)
