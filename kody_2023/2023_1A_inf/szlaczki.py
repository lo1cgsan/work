################
################
################
################

# dane wejściowe
szer = int(input("Podaj szerokość: "))
wys = int(input("Podaj wysokość: "))
znak = input("Podaj znak: ")

for j in range(wys):
    for i in range(szer):
        print(znak, end="")
    print()

################
#              #
#              #
################
print()
for j in range(wys):
    for i in range(szer):
        if j == 0 or j == wys-1:
            print(znak, end="")
        elif i == 0 or i == szer - 1:
            print(znak, end="")
        else:
            print(" ", end="")
    print()
