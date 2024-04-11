def fib_it(n):
    a, b = 0, 1 # przypisanie wielokrotne
    for i in range(n+1):
        print(a)
        #tmp = a
        #a = b
        #b = tmp + b
        a, b = b, a + b


def fib_while(n):
    a, b = 0, 1 # przypisanie wielokrotne
    while n > -1:
        print(a)
        a, b = b, a + b
        n -= 1

#a b
#  a b
#    a b
#      a b
#0 1 1 2 3 5 8 13 21

def main():
    n = int(input('Który wyraz ciągu? '))
    fib_it(n)
    fib_while(n)


main()
