from random import randint, seed

#seed(12345)

liczba = randint(1, 10)

"""
Napisz pętlę, która pobierze 5 liczb z klawiatury
i sprawdzi, czy użytkownik odgadł wylosowaną liczbę.
Jeżeli tak, wypisz "Zgadłeś" oraz wylosowaną liczbę.
"""
for i in range(5):
    a = int(input("Podaj liczbę: "))
    if a == liczba:
        print("Zgadłeś:", liczba)
        break # przerwanie działania pętli
