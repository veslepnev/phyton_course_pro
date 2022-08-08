a = input().split()
print(*sorted({i for i in a if a.count(i) > 1}))
