def index_of_nearest(numbers,number):
    if len(numbers) == 0:
        return -1
    a = list(map(lambda x: abs(x - number), numbers))
    return a.index(min(a))