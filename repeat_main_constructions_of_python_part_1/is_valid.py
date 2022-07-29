def is_valid(number):
    valid_len = [4, 5, 6]
    return len(number) in valid_len and " " not in number and number.isdigit()