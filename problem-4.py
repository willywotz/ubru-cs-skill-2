def run(text, key):
    o = ''
    n = 0
    a = ord('a')

    for i in text:
        if i == ' ':
            o += ' '
        else:
            o += chr((ord(key[n]) - a + ord(i) - a) % 26 + a)
            n = (n + 1) % len(key)

    return o

assert run('no pets', 'dog') == 'qc vhhy'
assert run('do not repeat yourself', 'zrtkp') == 'cf gyi qviops phegrvep'

print(run(input(), input()))
