def run(a, b):
    a = set(a.replace(',', '').split(' ')[1:])
    b = set(b.replace(',', '').split(' ')[1:])

    x = sorted(map(int, a ^ b))

    o = 'No Differences'

    if len(x) > 0:
        o = f"{len(x)} {', '.join(map(str, x))}"

    return o

assert run('4 7, 19, 1, 27', '5 7, 23, 14, 9, 27') == '5 1, 9, 14, 19, 23'
assert run('4 1, 2, 4, 3', '4 3, 2, 1, 4') == 'No Differences'
assert run('4 42, 5, 16, 1', '6 37, 84, 66, 30, 14, 5') == '8 1, 14, 16, 30, 37, 42, 66, 84'

print(run(input(), input()))
