# dane wejściowe
t1 = input("Podaj wyraz: ").lower().replace(" ", "")
t2 = input("Podaj wyraz: ").lower().replace(" ", "")

# Operacje na tekście
t1 = t1.lower()
t1 = t1.replace(" ", "")
t1 = t1.strip()

# operacje

if len(t1) != len(t2):
    print("Nie anagramy")
else:
    t1 = "".join(sorted(t1))
    t2 = "".join(sorted(t2))
    
    if t1 == t2:
        print("Angramy")
