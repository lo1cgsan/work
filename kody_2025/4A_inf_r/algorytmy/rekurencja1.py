
def gen_nieparzyste_it(n):
    for i in range(2*n):
        if i % 2 == 1:
            print(i)

# gen_nieparzyste_it(10)

def gen_nieparzyste_re(n):
    if n > 0:  # warunek brzegowy
        print(f'n = {n}')
        gen_nieparzyste_re(n-1)
        print(2 * n - 1)

# gen_nieparzyste_re(10)

def fib_re(n):
    if n < 3:
        return 1
    else:
        return fib_re(n-2) + fib_re(n-1)

n = int(input('Podaj numer wyrazu ciągu: '))
for i in range(1, n+1):
    print(fib_re(i))
