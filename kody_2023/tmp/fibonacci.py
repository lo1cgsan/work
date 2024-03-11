def fibonacci(n):
    a, b = 0, 1
    wynik = a + b
    for i in range(1, n):
        wynik = a + b
        a, b = b, wynik
    return wynik


n = int(input("Podaj numer wyrazu: "))
for i in range(1, n + 1):
    print(fibonacci_1(i))


