a = int(input("Podaj a: "))
b = int(input("Podaj b: "))

def nwd_1(a, b):
    licznik = 0
    while a != b:
        licznik = licznik + 1
        if a > b:
            a = a - b
        else:
            b = b - a

    print("Powtórzenia:", licznik)
    print(a)

nwd_1(a, b)

def nwd_2(a, b):
    licznik = 0
    while a > 0:
        licznik = licznik + 1
        a = a % b
        b = b - a

    print("Powtórzenia:", licznik)
    print(b)

nwd_2(a, b)
