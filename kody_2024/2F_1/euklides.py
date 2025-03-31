# euklides.py
a = int(input('Podaj a: '))
b = int(input('Podaj b: '))

def nwd1(a, b):
    while a != b:
        print(a, b)
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

def nwd2(a, b):
    while a > 0:
        print(a, b)
        a = a % b
        b = b - a
    return b

nwd = nwd1(a, b)
print(nwd, a // nwd, b // nwd)
print()
nwd = nwd2(a, b)
print(nwd, a // nwd, b // nwd)
