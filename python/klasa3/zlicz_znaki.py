def zlicz_znaki(tekst):
    licznik_liter = 0
    
    for znak in tekst:
        print(znak, ord(znak))
        #if (65 <= ord(znak) <= 90) or (97 <= ord(znak) <= 122):
        if znak.isalpha():
            licznik_liter += 1

    print("Litery:", licznik_liter)


def main():
    tekst = input("Podaj tekst: ")
    #print(tekst)
    zlicz_znaki(tekst)


main()





