def run(a):
    a = a.lower()

    a = list(a)
    b = set(a)

    o = 'pair isogram'

    for k in b:
        if a.count(k) % 2 != 0:
            o = 'NOT pair isogram'
            break

    return o

assert run('resTauratEurs') == 'NOT pair isogram'
assert run('aPpeareR') == 'pair isogram'
assert run('intestines') == 'pair isogram'
assert run('arRaiGniNg') == 'pair isogram'
assert run('installationS') == 'NOT pair isogram'
assert run('booKkeeper') == 'NOT pair isogram'

while True:
    a = input()
    if a == 'stop':
        break
    elif len(a) < 2:
        continue
    print(run(a))
