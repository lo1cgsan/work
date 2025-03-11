def znajdz_npnm(ciag):
    poczatek_sc = 0
    poczatek_nc = koniec_nc = 0
    for koniec_sc in range(1, len(ciag)):
        if ciag[koniec_sc] >= ciag[koniec_sc - 1]:  # mamy ciąg niemalejący
            if koniec_sc - poczatek_sc > koniec_nc - poczatek_nc:
                koniec_nc = koniec_sc
                poczatek_nc = poczatek_sc
        else:  # koniec ciągu niemalejącego, zaczynamy nowy ciąg
            poczatek_sc = koniec_sc
    return poczatek_nc, koniec_nc

dane = (23, 6, 7, 9, 11, 5, 90, 1, 35, 100)
indeks_p, indeks_k = znajdz_npnm(dane)
print(indeks_p, indeks_k)
print(dane[indeks_p:indeks_k + 1])
