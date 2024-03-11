from random import randint

liczba = randint(1, 10)

for i in range(3):
    typ = int(input("Podaj typ: "))
    if typ == liczba:
        print("Zgadłeś!")
    else:
        print("Próbuj dalej...")
