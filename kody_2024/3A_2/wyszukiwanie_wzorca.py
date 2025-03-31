# wyszukiwanie_wzorca.py
def znajdz_wzorzec(tekst, wzorzec, start):
    dl1 = len(tekst)
    dl2 = len(wzorzec)

    for i in range(start, dl1-dl2+1):
        for j in range(dl2):
            print(i, j, i+j)
            if tekst[i+j] != wzorzec[j]:
                break
        if tekst[i+j] == wzorzec[j]:
            return i
    return -1

tekst = 'informatyka'
wzorzec = 'forma'
indeks = znajdz_wzorzec(tekst, wzorzec, 0)
if indeks > 0:
    print('Znaleziono na pozycji:', indeks)
else:
    print('Nie znaleziono')
