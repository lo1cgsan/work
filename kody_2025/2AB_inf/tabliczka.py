# Napisz program, który wypisuje tabliczkę mnożenia do 5.
#
# 1 2 3 4 5
# 2 4 6 8 10
# 3 6 9 12 15
n = 10
for i in range(1, n+1):  # pętla zewnętrzna
    for j in range(1, n+1):  # pętla wewnętrzna, zagnieżdżona
        print(f'{i*j:4}', end=' ')
    print()

print()

znak = '#'
szer = 6
wys = 4

for i in range(wys):  # pętla zewnętrzna
    for j in range(szer):  # pętla wewnętrzna, zagnieżdżona
        print(znak, end=' ')
    print()
