n = int(input('Ilu studentów: '))

for i in range(n):
    liczba_p = int(input('Ile pytań: '))
    liczba_odp = int(input('Dobrych odpowiedzi: '))
    procent = liczba_odp / liczba_p * 100
    if procent >= 80:
        print("zaliczył")
    else:
        print("nie zaliczył")
