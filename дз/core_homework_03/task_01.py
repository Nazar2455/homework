from datetime import datetime

def get_days_from_today(date):
    date_not_string = datetime.strptime(date, "%Y-%m-%d")
    return (date_not_string - datetime.now()).days