# Napisz program, który wypisze na ekranie prostokąt o szerokości
# i wysokości podanej przez użytkownika za pomocą znaku podanego
# przez użytkownika.

znak = input("Podaj znak: ")
wys = int(input("Podaj wysokość: "))
szer = int(input("Podaj szerokość: "))

for i in range(wys):
    # print(szer * znak)
    for j in range(szer):
        if i == 0 or i == wys - 1:
            print(znak, end="")
        elif j == 0 or j == szer - 1:
            print(znak, end="")
        else:
            print(" ", end="")
    print()


for i in range(szer):
    print((i+1) * znak )

#
##
###
####
#####
######

   #
  ###
 #####
#######
