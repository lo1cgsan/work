# 1) Napisz funkcję while1(), która pobiera liczby wprowadzane przez
# użytkownika, aż do momentu, gdy ich suma przekroczy wartość 75.
# Na koniec program powinien wyświetlić liczbę i sumę wprowadzonych liczb.

def while1():
    # dane wejściowe
    suma = 0
    licznik = 0

    # obliczenia, operacje
    while suma <= 75:
        a = int(input("Podaj liczbę: "))
        suma = suma + a
        licznik += 1

    # dane wyjściowe
    print(licznik)
    print(suma)

while1()

# 2) Napisz funkcję, która pobiera od użytkownika liczby większe od 0, wartość 0 przerywa pobieranie. Program zlicza i drukuje, ile  wprowadzonych liczb jest nieparzystych.

def while2():
    # dane wejściowe
    pobierz a
    do licznik przypisz 0

    # obliczenia, operacje
    dopóki a > 0:
        jeżeli a % 2 równa się 1:
            zwiększ licznik o 1
            wypisz a
        pobierz a

    # dane wyjściowe
    wypisz licznik

while2()

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
