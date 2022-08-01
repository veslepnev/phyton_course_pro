def convert(string):
    small_letters = [i for i in string if i.islower()]
    big_letters = [i for i in string if i.isupper()]
    if len(small_letters) < len(big_letters):
        return string.upper()
    else:
         return string.lower()