from turtle import *

setup(800, 800, 0, 0)
ttl = Turtle()

def koch(bok, n):
    if n == 0:
        ttl.fd(bok)
        return
    koch(bok/3, n-1)
    ttl.left(60)
    koch(bok/3, n-1)
    ttl.right(120)
    koch(bok/3, n-1)
    ttl.left(60)
    koch(bok/3, n-1)

koch(400, 5)
# przykład rekurencji

def odliczanie(n):
    if n < 0:
        return
    print(n)
    odliczanie(n-1)
#    if n > 0:
#        odliczanie(n-1)
#    return
# odliczanie(6)
