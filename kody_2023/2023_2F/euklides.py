def euklides1(a, b):
    licznik = 0
    while a != b:
        licznik += 1
        if a > b:
            a = a - b
        else:
            b = b - a

    print("NWD =", a)
    print("Powtórzeń", licznik)


def euklides2(a, b):
    licznik = 0
    
    while a > 0:
        licznik += 1
        a = a % b
        b = b - a

    print("NWD =", b)
    print("Powtórzeń", licznik)

# dane wejściowe
a = int(input("Podaj a: "))
b = int(input("Podaj b: "))

euklides1(a, b)
euklides2(a, b)


# a = 10000, b = 2
# a = 10000 % 2 = 0, b = 2 - 0 = 2

