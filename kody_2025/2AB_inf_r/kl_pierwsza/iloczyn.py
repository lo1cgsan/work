# iloczyn.py
n = int(input('Ile liczb: '))
iloczyn = 1

for i in range(n):
    print('Powtórzenie:', i)
    a = int(input('Podaj liczbę: '))
    iloczyn = iloczyn * a
    print('Iloczyn:', iloczyn)

print(iloczyn)
