def fun(x):
    return x**2 - 4


def oblicz_pole(a, b, n):
    w = (b - a) / n
    x = a
    p = 0
    for i in range(1, n+1):
        x = a + w * i - w / 2
        p = p + w * fun(x)
    return p


def main():
    a = 5
    b = 10
    n = 1000
    print(oblicz_pole(a, b, n))

main()
