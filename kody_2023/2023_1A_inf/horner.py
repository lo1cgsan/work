# W(x) = a0*x^3 + a1*x^2 + a2*x + a3 => 6 mnożeń
# W(x) = (a0*x^2 + a1*x + a2)*x + a3
# W(x) = ((a0*x + a1)*x + a2)*x + a3 => 3 mnożeń

def horner_it(st, tb, x):
    wynik = tb[0]
    for i in range(st):
        wynik = wynik * x + tb[i+1]
    return wynik


def main():
    stopien = 3
    x = float(input('Podaj x: '))
    tb_wsp = []
    for i in range(stopien + 1):
        tb_wsp.append(float(input(f'Współczynnik {i}: ')))

    print(horner_it(stopien, tb_wsp, x))


main()
