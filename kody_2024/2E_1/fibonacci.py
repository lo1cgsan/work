def fib_for(n):
    a = 0
    b = 1
    for i in range(n+1):
        print(a)
        tmp = a
        a = b
        b = tmp + b
        if a > 0:
            print(b / a)


n = int(input('Podaj numer wyrazu ciągu: '))
fib_for(n)
