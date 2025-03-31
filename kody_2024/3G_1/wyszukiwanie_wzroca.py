# wyszukiwanie_wzroca.py
def znajdz_wzorzec(tekst, wzorzec, pozycja_startowa):
    dl1 = len(tekst)  # wyliczenie liczby znaków w tekście
    dl2 = len(wzorzec) # wyliczenie liczby znaków we wzorcu

    for i in range(pozycja_startowa, dl1-dl2+1):
        for j in range(dl2):
            if tekst[i+j] != wzorzec[j]:
                break
        if tekst[i+j] == wzorzec[j]:  # znaleziono wzorzec w tekście
            return i
    return -1  # wzorca nie znaleziono

indeks = znajdz_wzorzec('informatyka', 'rfor', 0)
print(indeks)
