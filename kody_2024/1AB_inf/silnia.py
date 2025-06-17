# silnia.py
n = int(input('Podaj liczbę: '))
# n! = 1 * 2 * ... * n
# 0! = 1
# 4! = 1 * 2 * 3 * 4 = 24

silnia = 1

for i in range(1, n+1):
    print('Powtórzenie:', i)
    silnia = silnia * i
    print('Iloczyn:', silnia)

print(silnia)
