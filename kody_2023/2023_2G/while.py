# 1) Napisz funkcję while1(), która pobiera liczby wprowadzane przez
# użytkownika, aż do momentu, gdy ich suma przekroczy wartość 75.
# Na koniec program powinien wyświetlić liczbę i sumę wprowadzonych liczb.

def while1():
    # dane wejściowe
    suma = 0
    licznik = 0

    # operacje
    while suma <= 75:
        a = int(input("Podaj liczbę: "))
        suma = suma + a
        licznik += 1

    # dane wyjściowe
    print(licznik)
    print(suma)


# 2) Napisz funkcję, któr pobiera od użytkownika liczby większe od 0, wartość 0 przerywa pobieranie. Program następnie zlicza i drukuje, ile wśród wprowadzonych liczb jest nieparzystych.

def while2():
    # dane wejściowe
    a = int(input("Podaj liczbę: "))
    licznik = 0

    # operacje
    while a > 0:
        if a % 2 == 1:
            licznik += 1
            print(a)

    # dane wyjściowe
    print(licznik)

3) Napisz program "while3.py", który pobiera od użytkownika znak i go wypisuje aż do momentu, gdy nie jest on literą 't', 'T', 'n', lub 'N'. Program wypisuje liczbę wprowadzonych znaków.

# dane wejściowe
pobierz znak
licznik

# obliczenia, operacje
dopóki znak != "t" or w2 or w3 or w4:
    wypisz znak
    zwiększ licznik
    pobierz znak

# dane wyjściowe
wypisz licznik
