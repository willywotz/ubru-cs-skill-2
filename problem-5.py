def run(a):
    (a, b) = list(map(int, a.split(', ')))
    (a, b) = (b, a) if a > b else (a, b)

    o = 0

    for i in range(a, b + 1):
        s = str(i)
        if s == s[::-1]:
            o += 1

    return o

assert run('55, 757') == 71
assert run('1, 1000000') == 1998
assert run('100, 1') == 18

print(run(input()))
