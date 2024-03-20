# generator liczb pseudolosowych
from random import randint, seed

# seed(12345)
szukana = randint(1, 10)

"""
Napisz program, który pobiera z klawiatury 5 liczb,
sprawdza czy podana liczba równa jest szukanej
i jeżeli tak wypisuje "Trafiłem:" oraz liczbę.
"""
n = 5
for i in range(n):
    a = int(input("Podaj liczbę: "))
    if a == szukana:
        print("Trafiona:", a)
        break # przewanie działania pętli


print("Szukana:", szukana)
