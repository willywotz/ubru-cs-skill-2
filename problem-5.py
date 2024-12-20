(a, b) = list(map(int, input().split(', ')))
(a, b) = (b, a) if a > b else (a, b)

o = 0

for i in range(a, b + 1):
    s = str(i)
    if s == s[::-1]:
        o += 1

print(o)
