# dane wejściowe
liczba_sztuk = [1, 3, 5, 1, 8, 2]
ceny = [23.7, 28.3, 19.5, 17.8, 11.8, 10.8]

# wynik dla kosztów opartych tylko na liczbie sztuk
for liczba in liczba_sztuk:
    if liczba < 3:
        print(10)
    else:
        print(17)

# wynik dla kosztów opartych na wartości zamówienia
n = len(liczba_sztuk)  # liczba klientów
for i in range(n):
    if liczba_sztuk[i] * ceny[i] < 20:
        print(12.5)
    else:
        print(9.9)
