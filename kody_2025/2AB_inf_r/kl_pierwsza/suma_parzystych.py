# Napisz program, który wypisze sumę liczb parzystych
# w zakresie <a, b> podanym przez użytkownika.

# dane wejściowe
a = int(input('Podaj a: '))
b = int(input('Podaj b: '))
dzielnik = int(input('Podaj dzielnik: '))

suma = 0
for i in range(a, b+1):
    if i % dzielnik == 0:
        suma = suma + i

print(suma)
