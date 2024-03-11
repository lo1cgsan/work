n = int(input("Podaj zakres: "))
iloczyn = 1
for liczba in range(1, n+1):
    print(iloczyn, "*", liczba)
    iloczyn = iloczyn * liczba
print(iloczyn)
