n = int(input("Podaj n: "))
m = int(input("Podaj m: "))

if n > 0 and m > 0 and m > n:
    for i in range(n, m + 1):
        print(i**2)
