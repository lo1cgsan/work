def potega_rek(a, n):
    if n == 0:
        return 1
    return potega_rek(a, n-1) * a


def silnia_rek(n):
    if n == 0:
        return 1
    return silnia_rek(n-1) * n


def nwd_rek(a, b):
    if b == 0:
        return a
    return nwd_rek(b, a % b)


print(potega_rek(2, 6))
print(potega_rek(3, 4))
print(silnia_rek(4))
print(nwd_rek(12, 48))
