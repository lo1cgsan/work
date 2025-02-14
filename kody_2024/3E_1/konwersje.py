def main():
    l_bin = input('Podaj liczbę binarną: ')
    n = len(l_bin)  # liczba cyfr

    l_dec = 0
    for cyfra in l_bin:
        wartosc = int(cyfra) * 2**(n-1)
        n = n - 1
        print(wartosc, "", end="")
        l_dec = l_dec + wartosc

    print()
    print(f"{l_bin}(2) = {l_dec}(10)")

main()
