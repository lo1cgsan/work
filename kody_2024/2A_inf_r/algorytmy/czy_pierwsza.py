def czy_pierwsza(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


n = int(input('Podaj liczbę: '))
assert czy_pierwsza(5) == True
assert czy_pierwsza(14) == False
assert czy_pierwsza(12) == False

# if czy_pierwsza(n) == True:
#    print('Pierwsza')
# else:
#    print('Niepierwsza')
