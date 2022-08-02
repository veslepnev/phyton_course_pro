def choose_plural(amount, declensions):
    if str(amount)[-1] == "1" and amount not in range(11, 912, 100):
        return f'{amount} {declensions[0]}'
    elif (str(amount)[-1] == "2" or str(amount)[-1] == "3" or str(amount)[-1] == "4") and \
            str(amount)[-2:] not in ["11", '12', '13', '14']:
        return f'{amount} {declensions[1]}'
    return f'{amount} {declensions[2]}'
