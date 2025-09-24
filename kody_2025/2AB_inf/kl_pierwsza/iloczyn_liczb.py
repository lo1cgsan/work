# Napisz program, który oblicza iloczyn liczb
# w zakresie (a, b) podanym przez użytkownika.
a = int(input('Podaj a: '))
b = int(input('Podaj b: '))

iloczyn = 1
for i in range(a+1, b):
    iloczyn = iloczyn * i
