from math import sqrt

def jest_pierwsza(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def main():
    for liczba in range(2, 101):
        if jest_pierwsza(liczba):
            print(f"Liczba {liczba} jest pierwsza.")
        else:
            print(f"Liczba {liczba} nie jest pierwsza.")

main()
