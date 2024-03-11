# a^n = a^n-1 * a dla >= 1
# a^n = 1 dla n = 0

def potega_rek(a, n):
    if n == 0:
        return 1
    return potega_rek(a, n-1) * a

# n! = (n-1)! * n dla n >= 1
# n! = 1 dla n = 0
def silnia_rek(n):
    if n == 0:
        return 1
    return silnia_rek(n-1) * n

a = 2
n = 5

# potega_rek(a, n)
print(silnia_rek(n))
