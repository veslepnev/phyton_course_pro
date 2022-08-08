n = int(input())
a = [sum(map(int, list(str(i)))) for i in range(1, n+1)]
b = [a.count(i) for i in a]
print(max(b))
