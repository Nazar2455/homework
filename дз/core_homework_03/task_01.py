from datetime import datetime
import re

def get_days_from_today(date):
    if date.replace("-","").isdigit() :
        date_not_string = datetime.strptime(date, "%Y-%m-%d")
        return (date_not_string - datetime.now()).days*-1-1
    else:
        print("Введено некоректну форму дати")

print(get_days_from_today("2024-07-09"))