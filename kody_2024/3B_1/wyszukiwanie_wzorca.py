# wyszukiwanie_wzorca.py
def znajdz_wzorzec(tekst, wzorzec, pozycja_startowa):
    dl1 = len(tekst)
    dl2 = len(wzorzec)

    for i in range(pozycja_startowa, dl1-dl2+1):
        for j in range(dl2):
            if tekst[i+j] != wzorzec[j]:
                break
        if tekst[i+j] == wzorzec[j]:
            return i
    return -1

wynik = znajdz_wzorzec('matematyka', 'ak', 0)
if wynik > -1:
    print('Znalazłem:', wynik)
else:
    print('Nie znalazłem')
