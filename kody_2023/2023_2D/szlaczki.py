# Napisz program, który wypisze prostokąt
# o szerokości i wysokości podanej przez użytkownika
# za pomocą podanego znaku.
# szer - liczbę znaków w wierszu
# wys - liczba wierszy

znak = input("Podaj znak: ")
szer = int(input("Podaj szerokość: "))
wys = int(input("Podaj wysokość: "))

for j in range(wys):
    for i in range(szer):
        if j == 0 or j == wys-1:
            print(znak, end="")
        elif i == 0 or i == szer-1:
            print(znak, end="")
        else:
            print(" ", end="")
    print()

######
#    #
#    #
#    #
#    #
######
