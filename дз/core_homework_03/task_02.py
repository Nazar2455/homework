import random

def get_numbers_ticket(min, max, quantity):
    all_nombers = []
    for i in range(min, max + 1):
        all_nombers.append(i)
    nombers = random.sample(all_nombers, quantity)
    return nombers 