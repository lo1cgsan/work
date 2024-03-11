# 1) Napisz program "while1.py", który pobiera liczby wprowadzane przez użytkownika, aż do momentu, gdy ich suma przekroczy wartość 75. Przed końcem program powinien wyświetlić sumę wprowadzonych liczb.

def while1():
    # dane wejściowe
    do suma przypisz 0

    # obliczenia, operacje
    dopóki suma jest mniejsza lub równa 75 wykonuj
        podaj a
        powiększ suma o a

    # dane wyjściowe
    wypisz suma

# 2) Napisz funkcję, któr pobiera od użytkownika liczby większe od 0, wartość 0 przerywa pobieranie. Program następnie zlicza i drukuje, ile wśród wprowadzonych liczb jest nieparzystych.

def while2():
    # dane wejściowe
    pobierz a
    do licznik przypisz 0

    # obliczenia, operacje
    dopóki a > 0:
        jeżeli a mod 2 równa się 1:
            zwiększ licznik o 1
            wypisz a

    # dane wyjściowe
    wypisz licznik

while1()
