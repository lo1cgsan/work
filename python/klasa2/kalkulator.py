#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  kalkulator.py

wynik = 0  # zmienna globalna

def pobierzLiczbe():
    ###
    Funkcja pobiera jedną liczbę całkowitą i zwraca ją
    ###
    liczba = int(input('Podaj liczbę: '))
    return liczba

def dodaj(l1, l2):
    global wynik
    wynik = l1 + l2

def odejmij(...):
    pass

def pomnoz(...):
    pass

def podziel(...):
    pass

def wydrukujWynik():
    ### Funkcja drukuje wynik obliczeń ###
    print('Wynik:', wynik)

def main(args):
    # 1) pobierz operację (+, -, /, *)
    op = input('Wpisz działanie (+, -, /, *): ')
    # 2) pobierz dwie liczby za pomocą funkcji
    liczba1 = pobierzLiczbe()
    liczba2 = pobierzLiczbe()
    #3) przekaz pobrane liczby do odpowiedniej funkcji, która obliczy wynik
    # działania

    if op == '+':
        dodaj(liczba1, liczba2)
    elif op == '-':
        pass
    elif op == '/':
        pass
    elif op == '*':
        pass
    else:
        print('Błędny znak działania!')

    4) wywołaj bezparametrową funkcję, która wydrukuje wynik
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
