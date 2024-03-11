def fmin(dane):
    w_min = 1
    for liczba in dane[1:]:
        if liczba < w_min:
            w_min = liczba
    print(w_min)


def fmax(dane):
    w_max = 1
    for liczba in dane[1:]:
        if liczba > w_max:
            w_max = liczba
    print(w_max)

dane = [1, 4, 3, 2, 4, 9, 5, 7]
n = 8

mniejsze = []
wieksze = []

for i in range(0, n, 2):
    if (dane[i] > dane[i + 1]):
        wieksze.append(dane[i])
        mniejsze.append(dane[i + 1])
    else:
        wieksze.append(dane[i + 1])
        mniejsze.append(dane[i])
        
print(mniejsze)
fmin(mniejsze)
print(wieksze)
fmax(wieksze)

        
# Powtórzeń: n - 1 + n - 1 = 2n - 2 = 14
# Powtórzeń: n / 2 + n / 2 - 1 + n / 2 - 1 = 3n/2 - 2 = 10
