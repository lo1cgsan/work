N = 7  # stała
a = [] # pusta lista
a = [0] * N  # lista N-elementowa wypełniona zerami

def czytaj():
    for i in range(N):
        # a.append(int(input('Podaj liczbę: ')))
        a[i] = int(input('Podaj liczbę: '))
    print(a)

def sumuj():
    suma = 0
    for i in range(N):
        # print(a[i])
        if i % 2 == 0:
            print(i, a[i])
            suma += a[i]
    print(suma)

def sumuj_2():
    suma2 = 0
    for el in a:
        # print(el)
        suma2 += el
    print(suma2)

def sumuj_co_n(krok):
    suma = 0
    for i in range(0, N, krok):
        # print(a[i])
        print(i, a[i])
        suma += a[i]
    print(suma)

czytaj()
sumuj_co_n(2)
