# Wypisz i policz liczby nieparzyste w zakresie <n;m> podanym przez użytkownika.

n = int(input('Podaj n: '))
m = int(input('Podaj m: '))

if n > m:
    print(list(range(n, m)))
    licznik = 0
    for i in range(n, m+1):
        if i % 2 == 1:
            print(i)
            licznik = licznik + 1
    print('Liczba nieparzystych:', licznik)
else:
    print('Błędne dane!')
