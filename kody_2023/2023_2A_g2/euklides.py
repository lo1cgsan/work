def euklides1(a, b):
    licznik = 0
    while a != b:
        licznik += 1
        if a > b:
            a = a - b
        else:
            b = b - a

    print(f"NWD = {a}")
    print(f"Powtórzeń: {licznik}")


def euklides2(a, b):
    licznik = 0
    if a < b:
        a, b = b, a
       
    while a > 0:
        licznik += 1
        a = a % b
        b = b - a

    print(f"NWD = {b}")
    print(f"Powtórzeń: {licznik}")


# dane wejściowe
a = int(input("Podaj liczbę a: "))
b = int(input("Podaj liczbę b: "))

# operacje i obliczenia
euklides1(a, b)
euklides2(a, b)

# dane wyjściowe
