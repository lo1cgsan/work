def licznik(x):
    # global x
    x = 7  # przesłonięcie zmiennej x

    x += 1
    for i in range(x):
        print(i)
    return x

x = 10
x = licznik(x)
print('x =', x)


