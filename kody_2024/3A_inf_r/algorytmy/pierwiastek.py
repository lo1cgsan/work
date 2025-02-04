def pierwiastek(p, d):
    a = p
    while a - p / a > d:
        print(a)
        a = (a + p / a) / 2
    return a


def main():
    x = float(input('Podaj liczbę: '))
    d = float(input('Podaj dokładność: '))
    print(pierwiastek(x, d))


main()
