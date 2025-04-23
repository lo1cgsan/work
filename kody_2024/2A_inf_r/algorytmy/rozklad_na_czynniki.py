# 20 = 2 * 2 * 5 = 2^2 * 5
# 248 = 2 * 2 * 2 * 31 = 2^3 * 31
"""
56 / 2
28 / 2
14 / 2
7 / 7
1
"""

def rozloz(n):
    czynniki = []
    k = 2
    while n != 1:
        while n % k == 0:
            n = n // k
            czynniki.append(k)
        k = k + 1
    return czynniki

def main():
    n = 248
    print(rozloz(n))

main()
