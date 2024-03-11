# Napisz program, który wypisuje prostokąt
# o podanej szerokości i wysokości
# za pomocą podanego znaku.
# szer – liczba znaków w wierszu
# wys – liczba wierszy

znak = input("Podaj znak: ")
szer = int(input("Podaj szerokość: "))
wys = int(input("Podaj wysokość: "))

for j in range(wys):
    # print(szer * znak)
    for i in range(szer):
        print(znak, end="")
    print()

###########
###########
###########
###########
###########

print()

for j in range(wys):
    # print("Wiersz:", j)
    for i in range(szer):
        if j == 0 or j == wys - 1:     # pierwszy lub ostatni wiersz
            print(znak, end="")
        elif i == 0 or i == szer - 1:  # pierwsza lub ostatnia kolumna
            print(znak, end="")
        else:                          # środkowa kolumna
            print(" ", end="")
    print()

###########
#         #
#         #
#         #
#         #
###########
