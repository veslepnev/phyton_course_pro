a = [input().split(', ') for i in range(int(input()))]
result = {}
for i in a:
    for j in i:
        result[j] = result.get(j, 0) + 1
b = [i for i in result if result[i] == len(a)]
if any(b):
    print(*sorted(b), sep=', ')
else:
    print("Сериал снять не удастся")
