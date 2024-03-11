sw = int(input("Podaj liczbę wszystkich samochodów: "))
p = float(input("Podaj procent rocznej produkcji s. dostawczych: "))

so = (p * sw) / 100
so = sw - (p * sw) / 100

print("Liczba s. osobowych", int(so))

