def fib_for(n):
    a = 0
    b = 1
    for i in range(n+1):
        print(a)
        tmp = a
        a = b
        b = tmp + b
    print(a, b)

#a b
#  a b
#    a b
#      a b
#0 1 1 2 3
#
#
def main():
    n = int(input('Który wyraz ciągu? '))
    fib_for(n)


main()
