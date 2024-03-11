def rysuj_prostokat(n, m, znak):
    for i in range(n):  # wysokość
        for j in range(m):  # szerokość
            print(znak, end="")
        print()

def rysuj_prostokat_pusty(n, m, znak):
    for i in range(n):  # drukowanie wierszy
        for j in range(m):  # drukowanie kolumn
            if i == 0 or i == n-1:  # sprawdzanie wiersza
                print(znak, end="")
            elif j == 0 or j == m-1:  # sprawdzanie kolumny
                print(znak, end="")
            else:
                print(" ", end="")  # drukowanie spacji
        print()

# pobranie danych wejściowych
n = int(input("Podaj wysokość: "))
m = int(input("Podaj szerokość: "))
znak = input("Podaj znak: ")

# wywołanie funkcji
rysuj_prostokat_pusty(n, m, znak)

# ******\n
# ******\n
# ******\n
# ******\n
# ******\n

# ******\n
# *    *\n
# *    *\n
# *    *\n
# ******\n
