# choinka.py

#
##
###
####
#####
######

znak = input('Podaj znak: ')
n = int(input('Ile kolumn: '))
m = int(input('Ile wierszy: '))

for j in range(m):
    for i in range(n):
        if j == 0 or j == m-1:
            print(znak, end='')
        elif i == 0 or i == n-1:
            print(znak, end='')
        else:
            print(' ', end='')
    print()
