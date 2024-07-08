import random

def get_numbers_ticket(min, max, quantity):
    if max - min >= quantity - 1 and max > min:   
        all_nombers = []
        for i in range(min, max + 1):
            all_nombers.append(i)
        nombers = random.sample(all_nombers, quantity)
        nombers.sort()
        return nombers
    else:
        print("Введено некоректні параметри")

print(get_numbers_ticket(1,6,7))