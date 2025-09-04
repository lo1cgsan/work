# dane wejściowe

def wydaj_reszte(nominaly, reszta):
    while reszta > 0:
        # for i in range(len(nominaly)):
        #    nominaly[i]
        for n in nominaly:
            if n < reszta:
                break
        l_nominalow = reszta // n
        print(n, l_nominalow)
        reszta -= l_nominalow * n


def main():
    nominaly = (50, 20, 10, 5, 2, 1)
    reszta = int(input('Podaj resztę: '))
    wydaj_reszte(nominaly, reszta)

main()