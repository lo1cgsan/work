n = int(input("Podaj liczbę: "))

# 1) wypisz liczby od 1 do n
for i in range(1, n+1):
    print(i)

# 2) zlicz liczby parzyste od 1 do n i wypisz je
for i in range(1, n+1):
    if i % 2 == 0:
        print(i)

# 3) zlicz liczby 2-cyfrowe od 1 do n i wypisz je
for i in range(1, n+1):
