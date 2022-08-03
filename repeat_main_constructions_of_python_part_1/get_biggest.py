def get_biggest(numbers):
    if not numbers:
        return -1
    else:
        return int("".join(sorted(map(str, numbers), key=lambda x: str(x) * max(numbers), reverse=True)))
