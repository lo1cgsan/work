def euklides1(a, b):
    licznik = 0

    # obliczenia
    while a != b:
        licznik += 1
        if a > b:
            a = a - b
        else:
            b = b - a

    print("NWD =", a)
    print("Powtórzeń:", licznik)


def euklides2(a, b):
    licznik = 0
    
    while a > 0:
        licznik += 1
        a = a % b
        b = b - a
    
    print("NWD =", b)
    print("Powtórzeń:", licznik)

# a = 1000000, b = 2
# a = 1000000 % 2 = 0, b = 2 - 0 = 2
    
    
# dane wejściowe
a = int(input("Podaj a: "))
while a <= 0:
    print("Błędne dane!")
    a = int(input("Podaj a: "))
b = int(input("Podaj b: "))

# wywołanie funkcji
euklides1(a, b)
euklides2(a, b)

