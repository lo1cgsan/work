def wypisz_parzyste_1():
    # funkcja bez parametrów, nie zwracająca wartości
    for i in range(1, 101):
        if i % 2 == 0:
            print(i, "", end="")

def wypisz_parzyste_2(n):
    # funkcja z parametrem, nie zwracająca wartości
    for i in range(1, n):
        if i % 2 == 0:
            print(i, "", end="")

def wypisz_parzyste_3(n):
    # funkcja z parametrem, zwracająca wartość
    licznik = 0
    for i in range(1, n):
        if i % 2 == 0:
            print(i, "", end="")
            licznik += 1
    return licznik


