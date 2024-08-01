import random


def get_numbers_ticket(min, max, quantity):
    ticket = []

    for num in range(1):
        if min < 1 or max > 1000 or quantity < 1 or quantity > (max - min + 1):
            return []

        ticket = random.sample(range(min, max + 1), quantity)

    ticket.sort()
    return ticket

print(get_numbers_ticket(1, 50, 6))
