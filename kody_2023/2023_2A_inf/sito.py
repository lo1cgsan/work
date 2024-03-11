from math import sqrt

MAX_N = 100
sito = [True] * MAX_N

for i in range(2, int(sqrt(MAX_N)) + 1):
    if sito[i]:
        j = i + i
        while j <= MAX_N-1:
            sito[j] = False
            j = j + i

for i in range(2, MAX_N):
    if sito[i]:
        print(i, end=' ')

