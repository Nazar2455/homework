import re

def  normalize_phone(phone_number):
    phone_number = re.sub(r"\D", "", phone_number)
    a = re.search("380", phone_number)
    if a:
        return "+" + phone_number
    else:
        return "+38" + phone_number