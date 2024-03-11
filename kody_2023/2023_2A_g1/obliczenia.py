from matfun import potega
from matfun import silnia

a = int(input("Podaj a: "))
n = int(input("Podaj n: "))

print(potega(a, n))
p1 = potega(a, n)
print(p1)
p2 = potega(2, 8) + potega(2, 5)
print(p2)


print(silnia(a))
