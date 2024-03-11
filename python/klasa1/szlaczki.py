# Napisz program, któ©y wypisuje w terminalu prostokąt
# o podanej wysokości i szerokości z użyciem podanego znaku.
#
# wys = 6, szer = 5

znak = input("Podaj znak: ")
wys = int(input("Podaj wysokość: "))
szer = int(input("Podaj szerokość: "))

for i in range(wys): # pętla wierszy
    for j in range(szer): # pętla kolumn
        if i == 0 or i == wys-1:
            print(znak, end="")
        elif j == 0 or j == szer-1:
            print(znak, end="")
        else:
            print(" ", end="")
    print()  # przejście do nowego wiersza

#####
#   #
#   #
#   #
#   #
#####

exit()
for i in range(wys):
    print(szer * znak)
