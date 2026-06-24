from math import sqrt, floor

MAX_N = 64000

n = int(input(f'Podaj n (<={MAX_N}): '))
# sprawdzenie poprawności
sito = [True] * n
sito[0:2] = [False, False]
sqrt_n = floor(sqrt(n))

for i in range(2, sqrt_n+1):
    if sito[i]:
        # j = i + i
        # while j < n:
            # sito[j] = False
            # j += i
        for j in range(i+i, n, i):
            sito[j] = False

for i in range(2, n):
    if sito[i]:
        print(i, end=' ')
