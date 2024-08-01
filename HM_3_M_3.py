import re

phone_number = input(f"Add your phone number: ")


def normalize_phone(phone_number):
    clean_numbers = re.sub(r'\D', '', phone_number)
    if not clean_numbers.startswith('+'):
        if clean_numbers.startswith("380"):
                clean_numbers = "+" + clean_numbers
        else:
            clean_numbers = "+38" + clean_numbers
    return clean_numbers

print (normalize_phone(phone_number))
