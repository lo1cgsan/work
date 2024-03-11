# dane wejściowe
tekst = input("Podaj tekst: ")
tekst = tekst.lower().replace(" ", "")

# operacje
dl = len(tekst)
tekst2 = ""
for i in range(dl-1, -1, -1):
    tekst2 = tekst2 + tekst[i]

if tekst == tekst2:
    print("Palindrom")
else:
    print("Niepalindrom")
