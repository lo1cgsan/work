def f(s):
    """Funkcja zwraca sumę kodów ASCII podanego słowa s"""
    wynik = 0
    for z in s:
        wynik += ord(z)
    return wynik

def d(x, s):
    """Zwraca liczbę wystąpień litery x w słowie s"""
    wynik = 0
    for z in s:
        if z == x:
            wynik += 1
    return wynik
    # return s.count(x)

def w(x, s1, s2):
    """Zwraca mniejszą liczbę wystąpień litery x w słowach s1 i s2"""
    ile_1 = d(x, s1)
    ile_2 = d(x, s2)
    if ile_1 < ile_2:
        return ile_1
    return ile_2
    # return min(s1.count(x), s2.count(x))

def w_s(x, s):
    """Zwraca True, jeśli litera x znajduje się w słowie s"""
    for z in s:
        if z == x:
            return True

def sumuj_unikalne(s1, s2):
    """Zwraca sumę unikalnych znaków dla słów s1 i s2"""
    znaki = ''
    suma = 0
    for z in s1:
        if not d(z, znaki):
            znaki += z
            suma += w(z, s1, s2)
    print(suma)
    return suma

def ps(s1, s2):
    n = len(s1)
    ps_1 = ''
    if len(s1) > len(s2):
        n = len(s2)
    print(s1, s2, n)
    for i in range(n):
        if s1[i] == s2[-1-i]:
            ps_1 += s1[i]
    return ps_1

def prefiksosufiks(s1, s2):
    ps_1 = ps(s1, s2)
    ps_2 = ps(s2, s1)
    if len(ps_1) > len(ps_2):
        print(ps_1)
        return len(ps_1)
    else:
        print(ps_2)
        return len(ps_2)

with open('pary.txt') as plik:
    suma_maks = -1
    for wiersz in plik:
        wiersz = wiersz.strip().split(' ')
        s1, s2 = wiersz[0], wiersz[1]
        dl = prefiksosufiks(s1, s2)
        print(dl)
# zad 3.2
#        if len(s1) < len(s2):
#            suma = sumuj_unikalne(s1, s2)
#        else:
#            suma = sumuj_unikalne(s2, s1)
#        if suma > suma_maks:
#            suma_maks = suma
# zad 3.1
#        print(f(s1), f(s2))
#        suma = f(s1) - f(s2)
#        if suma < 1:
#            suma *= -1
#        if suma > suma_maks:
#            suma_maks = suma

print(suma_maks)
