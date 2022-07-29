def hide_card(card):
    a = "".join(card.split())
    return '*' * 12 + a[12:]