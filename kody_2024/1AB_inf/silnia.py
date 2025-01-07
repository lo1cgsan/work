# silnia.py
n = int(input('Podaj liczbę: '))
# n! = 1 * 2 * ... * n
# 0! = 1
# 4! = 1 * 2 * 3 * 4 = 24

iloczyn = 1

for i in range(1, n+1):
    print('Powtórzenie:', i)
    iloczyn = iloczyn * i
    print('Iloczyn:', iloczyn)

print(iloczyn)
