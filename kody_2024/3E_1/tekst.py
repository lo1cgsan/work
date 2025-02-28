tekst = input('Podaj tekst: ')
print(tekst)

n = len(tekst)  # liczba znaków w tekście
for i in range(n):
    print(tekst[n-1-i])
