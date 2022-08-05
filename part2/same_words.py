def replace1(word):
    q = ''
    for i in word:
        if i in a:
            q += "1"
        elif i in b:
            q += "2"
    return q


a = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']
b = 'б, в, г, д, ж, з, й, к, л, м, н, п, р, с, т, ф, х, ц, ч, ш, щ, ь'.replace(',', '').split()
word = input()
list_of_words = [input() for i in range(int(input()))]
list_of_words2 = list(map(lambda x: replace1(x)[:len(replace1(x)) - replace1(x)[::-1].find('1')], list_of_words))
result = dict(zip(list_of_words, list_of_words2))
result1 = [i for i, k in result.items() if replace1(word)[:len(replace1(word)) - replace1(word)[::-1].find('1')] == k]
print(*result1, sep="\n")