# lista wielowymiarowa
n = 3
m = 3

A = [
    [1,  1, 1],
    [0, 1, 0],
    [1,  1, 1]
]

P = [
    [True, True, True],
    [False, True, False],
    [False, True, True]
]

P[0][0] = True
print(P)

for i in range(n):
    for j in range(m):
        # i = 2, j = 2
        if A[i][j] == 0:
            P[i][j] = False
        else:
            # jeżeli 1 wiersz i nie 1 kolumna
            if i == 0 and j > 0:
                P[i][j] = P[i][j - 1]
            # jeżeli nie 1 wiersz i 1 kolumna
            if i > 0 and j == 0:
                P[i][j] = P[i - 1][j]
            # jeżeli nie 1 wiersz i nie 1 kolumna
            if i > 0 and j > 0:
                P[i][j] = P[i][j - 1] or P[i - 1][j]


for i in range(n):
    for j in range(m):
        print(P[i][j], end=" ")
    print()
