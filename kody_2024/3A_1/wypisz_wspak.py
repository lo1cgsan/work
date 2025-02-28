tekst = input('Podaj tekst: ')
n = len(tekst)

#for i in range(n):
#    print(tekst[n-1-i])
#    print(tekst[-1-i])

for i in range(-1, -n-1, -1):
    print(tekst[i])


