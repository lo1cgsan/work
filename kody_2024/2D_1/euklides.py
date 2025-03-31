def nwd1(a, b):
    while a != b:  # dopóki a jest różne od b
        print(a, b)
        if a > b:
            a = a - b
        else:
            b = b - a
    print(a)

def nwd2(a, b):
    while a > 0:
        print(a, b)
        a = a % b
        b = b - a
    return b
        

a = int(input('Podaj licznik: '))
b = int(input('Podaj mianownik: '))

# użycie funkcji nwd2()
nwd = nwd2(a, b)
print(nwd)
# wypisz skrócony ułamek a / b
print(a // nwd, '/', b // nwd)

a = a // nwd
b = b // nwd
print(f'{a} / {b}')


