def pobierz_liczby():
    x = float(input("Podaj liczbę a: "))
    y = float(input("Podaj liczbę b: "))
    return x, y

def dodaj(a, b):
    print("Suma:", a + b)

def odejmij(a, b):
    print("Różnica:", a - b)

def pomnoz(a, b):
    print("Iloczyn:", a * b)

def podziel(a, b):
    if b == 0:
        print('Nie wolno dzielić przez zero!')
        return
    print("Iloraz:", a / b)


def main():
    wybor = ""
    while wybor != "q":
        wybor = input("""
        Witaj w kalulatorze. Wybierz operację:
        +) dodawanie
        -) odejmowanie
        *) mnożenie
        /) dzielenie
        q) zakończ

        """)
        a, b = pobierz_liczby()
        if wybor == "+":
            dodaj(a, b)
        elif wybor == "-":
            odejmij(a, b)
        elif wybor == "*":
            pomnoz(a, b)
        elif wybor == "/":
            podziel(a, b)
        elif wybor != "q":
            print("Błędna operacja...")
            
main()
