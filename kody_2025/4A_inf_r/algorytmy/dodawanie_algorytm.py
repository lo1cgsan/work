a = '734'
b = '675'

wynik = []
p = 0

for i in range(len(a) - 1, -1, -1):
    d = int(a[i]) + int(b[i]) + p
    c = d % 10
    p = d// 10
    wynik.append(c)
    # i += 1
if p != 0:
    wynik.append(p)

# wynik.reverse()
print(wynik)

n = len(wynik)
suma = 0
for i in range(n - 1, -1, -1):
    suma += wynik[i] * 10**i

print(suma)
