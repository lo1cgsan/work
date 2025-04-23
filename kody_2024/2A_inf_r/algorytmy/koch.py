from turtle import *

setup(800, 800, 0, 0)
ttl = Turtle()

def koch0(bok):
    ttl.fd(bok)

def koch1(bok):
    koch0(bok/3)
    ttl.left(60)
    koch0(bok/3)
    ttl.right(120)
    koch0(bok/3)
    ttl.left(60)
    koch0(bok/3)

def koch2(bok):
    koch1(bok/3)
    ttl.left(60)
    koch1(bok/3)
    ttl.right(120)
    koch1(bok/3)
    ttl.left(60)
    koch1(bok/3)

def koch3(bok):
    koch2(bok/3)
    ttl.left(60)
    koch2(bok/3)
    ttl.right(120)
    koch2(bok/3)
    ttl.left(60)
    koch2(bok/3)

def koch4()

def koch5()

def koch6()

bok = 300
koch3(bok)
done()
