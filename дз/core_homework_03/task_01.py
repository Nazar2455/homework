from datetime import datetime
import re

def get_days_from_today(date):
    try:
        date_not_string = datetime.strptime(date, "%Y-%m-%d")
        return (date_not_string - datetime.now()).days*-1-1
    except:
        print("Введено некоректну форму дати")