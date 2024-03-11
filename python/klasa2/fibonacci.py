def fib_it(n):
    a = 0
    b = 1
    for i in range(n):
        # print(a)
        tmp = b
        b = a + b
        a = tmp
    return a

def main():
    n = int(input("Podaj numer wyrazu: "))
    print(f"{n} = {fib_it(n)}")
    for i in range(2, 21):
        print(fib_it(i) / fib_it(i-1))


main()
