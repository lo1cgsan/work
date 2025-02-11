def bin2dec(l_bin, p):
    l_dec = 0
    n = len(l_bin)
    for cyfra in l_bin:
        wartosc = int(cyfra) * p**(n-1)
        n = n - 1
        print(wartosc, "", end="")
        l_dec = l_dec + wartosc

    return l_dec

def main():
    l_bin = input('Podaj liczbę binarną: ')

    l_dec = bin2dec(l_bin, 2)
    print()
    print(f"{l_bin}(2) = {l_dec}(10)")

main()
