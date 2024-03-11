def main():
    imie = "Julia"
    print(imie)
    print(type(imie))

    wiek = 16
    print(wiek)
    print(type(wiek))

    # ocena1 = 3
    ocena1 = int(input("Podaj ocenę: "))
    print(type(ocena1))
    ocena2 = 5
    ocena3 = 2
    
    srednia = (ocena1 + ocena2 + ocena3) / 3
    print(srednia)
    print(type(srednia))

    print("Witaj", imie, ", masz", wiek, "lat!")
    print(f"Witaj {imie}, masz {wiek} lat!")
    

    return 0

main()
