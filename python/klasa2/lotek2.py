from random import randint

liczba = randint(1, 100)

typ = int(input("Podaj typ: "))

while typ != liczba:
    print("Próbuj dalej...")
    typ = int(input("Podaj typ: "))

print("Zgadłeś!")
