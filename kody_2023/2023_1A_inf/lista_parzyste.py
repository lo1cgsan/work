"""
Napisz program, który pobiera od użytkownika 10 liczb
i zapisuje je w liście. Następnie napisz i użyj funkcji
policz_parzyste(), która zlicza i sumuje liczby parzyste
zapisane w liście. Wypisz liczbę i sumę.
"""
def policz_parzyste(lista):
    licznik = 0
    suma = 0
    for x in lista:
        if x % 2 == 0:
            licznik = licznik + 1 # inkrementacja
            suma = suma + x
    print('Liczba:', licznik, 'Suma:', suma)


def main():
    lista = []
    for i in range(10):
        liczba = int(input('Podaj liczbę: '))
        lista.append(liczba)
    print(lista)
    policz_parzyste(lista)


main() # wywołanie funkcji
