import re

phone_number = [
"    +38(050)123-32-34",
"     0503451234",
"(050)8889900",
"38050-111-22-22",
"38050 111 22 11   "]


def normalize_phone(phone_number):
    new_numbers = []
    for phone in phone_number:
        clean_numbers = re.sub(r'\D', '', phone)
        if not clean_numbers.startswith('+'):
            if clean_numbers.startswith("380"):
                new_numbers.append(clean_numbers)
            else:
                clean_numbers = "+38" + clean_numbers
        new_numbers.append(clean_numbers)
    return new_numbers

normalize_phone(phone_number)