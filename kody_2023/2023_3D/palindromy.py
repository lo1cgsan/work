# dane wejściowe
wyraz = input("Podaj tekst: ").lower().replace(" ", "")
dl = len(wyraz)
wyraz2 = ""

# operacje

for i in range(dl - 1, -1, -1):
    wyraz2 = wyraz2 + wyraz[i]

# wyniki
if wyraz == wyraz2:
    print("Palindromy")
else:
    pritn("Nie palindromy")

