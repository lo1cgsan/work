def fib_for(n):
    fn1 = 0
    fn2 = 1

    for i in range(n+1):
        print(fn1)
        tmp = fn1
        fn1 = fn2
        fn2 = tmp + fn2
        print(fn2/fn1)

n = int(input('Podaj numer wyrazu ciągu: '))
fib_for(n)
