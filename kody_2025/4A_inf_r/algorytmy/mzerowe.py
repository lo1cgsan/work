def fun1(x):
    return 2 * x - 4

def fun2(x):
    return 2 * x**2 - 4 * x

def m_zerowe(a, b, dokladnosc, f):
    while b - a > dokladnosc and f(a) != 0 and f(b) != 0:
        c = (a + b) / 2
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

    if f(a) == 0:
       return a
    if f(b) == 0:
        return b
    return c


def main():
    f = fun2
    lewy = prawy = 0
    while f(lewy) * f(prawy) > 0 or prawy <= lewy:
        lewy = float(input('Podaj lewy: '))
        prawy = float(input('Podaj prawy: '))
    d = 0.1
    wynik = m_zerowe(lewy, prawy, d, f)
    print(wynik, f(wynik ))


main()