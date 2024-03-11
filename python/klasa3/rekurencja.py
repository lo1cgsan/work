def potega_it(x, n):
    wynik = 1
    for i in range(n):
        wynik = wynik * x
    return wynik

def potega_re(x, n):
    # x^0 = 1
    # x^n = x^(n-1) * x
    if n == 0:
        return 1
    return potega_re(x, n-1) * x

#1) potega_re(2, 4) = 2^3 * 2
#2) potega_re(2, 3) * 2 = 2^2 * 2
#3) potega_re(2, 2) * 2 = 2^1 * 2
#4) potega_re(2, 1) * 2 = 2^0 * 2
#5) potega_re(2, 0) * 2 = 1
#4) potega_re(2, 1) * 2 = 1 * 2
#3) potega_re(2, 2) * 2 = 1 * 2 * 2
#2) potega_re(2, 3) * 2 = 1 * 2 * 2 * 2
#1) potega_re(2, 4) = 1 * 2 * 2 * 2 * 2

#STOS = [2, 4, 2,
#        2, 3, 2, 
#        2, 2, 2, 
#        2, 1, 2, 
#        2, 0, 2]

print(potega_it(2, 4))
print(potega_re(2, 4))

def silnia_it(n):
    wynik = 1
    for i in range(1, n + 1):
        wynik = wynik * i
    return wynik

def silnia_re(n):
    if n == 0:
        return 1
    return silnia_re(n-1) * n

print(silnia_it(4))
print(silnia_re(4))
