def dodaj():
    a = float(input("Podaj liczbę a: "))
    b = float(input("Podaj liczbę b: "))
    print("Suma:", a + b)

def odejmij():
    a = float(input("Podaj liczbę a: "))
    b = float(input("Podaj liczbę b: "))
    print("Różnica:", a - b)

def pomnoz():
    a = float(input("Podaj liczbę a: "))
    b = float(input("Podaj liczbę b: "))
    print("Iloczyn:", a * b)

def podziel():
    a = float(input("Podaj liczbę a: "))
    b = float(input("Podaj liczbę b: "))
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
        if wybor == "+":
            dodaj()
        elif wybor == "-":
            odejmij()
        elif wybor == "*":
            pomnoz()
        elif wybor == "/":
            podziel()
        elif wybor != "q":
            print("Błędna operacja...")
            
main()
