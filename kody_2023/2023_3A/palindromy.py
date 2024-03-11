# dane wejściowe
wyraz = input("Podaj wyraz: ").lower().replace(" ", "")

wyraz2 = ""

for i in range(len(wyraz) - 1, -1, -1):
    wyraz2 += wyraz[i]
    
if wyraz == wyraz2:
    print("Palindromy")
else:
    print("Nie palindromy")

dl = len(wyraz)
for i in range(dl // 2):
    if wyraz[i] != wyraz[dl - 1 - i]:
        print("Nie palindromy")
        exit()

print("Palindromy")
