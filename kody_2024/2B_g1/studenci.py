# dane wejściowe

n = int(input("Podaj liczbę studentów: "))
prog = int(input("Próg zaliczenia: "))

# operacje
liczba_pytan = int(input("Liczba pytań: "))
dobre_odpowiedzi = int(input("Dobre odpowiedzi: "))

procent = dobre_odpowiedzi / liczba_pytan * 100
print(procent)

if procent >= prog:
    zdal = True
else:
    zdal = False

# dane wyjściowe, tj. wynik
if zdal == True:
    print("Zdał")
else:
    print("nie zdał")
