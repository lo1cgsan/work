def nwd1(a, b):
    while a != b:  # dopóki a jest różne od b
        if a > b:
            a = a - b
        else:
            b = b - a

    print(a)

a = int(input('Podaj a: '))
b = int(input('Podaj b: '))

# użycie funkcji nwd1()
nwd1(a, b)
