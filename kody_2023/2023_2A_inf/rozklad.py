def rozloz(n):
    czynniki = []
    k = 2
    while n > 1:
        while n % k == 0:
            czynniki.append(k)
            n = n // k
        k = k + 1
    return czynniki

n = int(input("Podaj liczbę: "))
print(rozloz(n))
