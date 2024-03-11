# pobranie liczby z klawiatury i zapisanie jej w zmiennej
liczba = input("Podaj liczbę: ")

# sprawdzanie czy liczba jest parzysta
if int(liczba) % 2 == 0:
    print("Liczba", liczba)
    print("Parzysta")
else:
    print("Nieparzysta")

