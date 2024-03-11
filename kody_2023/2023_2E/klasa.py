pkt = int(input("Podaj liczbę punktów: "))
f = float(input("Podaj frekwencję: "))
so = float(input("Podaj średnią ocen: "))

if f > 0.94 and so >= 4.0:
    pkt = pkt + 20

print("Liczba punktów:", pkt)
