wyraz = input("Podaj tekst: ")

# wypisz wyraz wspak
print(wyraz[::-1])


d = len(wyraz)
for i in range(d - 1, -1, -1):
    print(wyraz[i])
