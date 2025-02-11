def wypisz_nieparzyste_1():
    # funkcja bez parametrów, nie zwracająca wartości
    for i in range(1, 101):
        if i % 2 == 0:
            print(i, "", end="")

def wypisz_nieparzyste_2(n):
    # funkcja z parametrem, nie zwracająca wartości
    for i in range(1, n):
        if i % 2 == 0:
            print(i, "", end="")

wypisz_nieparzyste_2(50)
print()
wypisz_nieparzyste_2(20)
