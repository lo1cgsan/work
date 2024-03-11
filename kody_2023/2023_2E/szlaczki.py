znak = input("Podaj znak: ")
szer = int(input("Podaj szerokość: "))
wys = int(input("Podaj wysokość: "))

for i in range(wys):  # pętla wierszy
    # print("Wiersz:", i)
    for j in range(szer):  # pętla kolumn
        if i == 0 or i == wys-1:  # pierwszy wiersz lub ostatni
            print(znak, end="")
        elif j == 0 or j == szer-1:  # pierwsza lub ostatnia kolumna
            print(znak, end="")
        else:
            print(" ", end="")
    print()  # przejście do nowego wiersza

######
#    #
#    #
#    #
######
