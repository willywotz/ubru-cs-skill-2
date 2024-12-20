base = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def col(n):
    if n == 0:
        return ''
    return col((n - 1) // 26) + base[(n - 1) % 26]

def run(a):
    a = a.lower()

    (r, c) = a[1:].split('c')
    o = f"{col(int(c))}{r}"

    return o

assert run('r1c1') == 'A1'
assert run('r3c1') == 'A3'
assert run('r5c26') == 'Z5'

while True:
    a = input()
    if a == 'r0c0':
        break
    print(run(a))
