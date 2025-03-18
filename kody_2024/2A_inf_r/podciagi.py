def znajdz_npnm(ciag):
    poczatek_sc = 0
    poczatek_nc = koniec_nc = 0
    for koniec_sc in range(1, len(ciag)):
        if ciag[koniec_sc] >= ciag[koniec_sc - 1]:  # mamy ciąg niemalejący
            if koniec_sc - poczatek_sc > koniec_nc - poczatek_nc:
                print(poczatek_nc, koniec_nc)
                koniec_nc = koniec_sc
                poczatek_nc = poczatek_sc
        else:  # koniec ciągu niemalejącego, zaczynamy nowy ciąg
            poczatek_sc = koniec_sc
    return poczatek_nc, koniec_nc

def znajdz_npnm_suma(ciag):
    """Znajdowanie spójnego podciągu o największej sumie"""
    poczatek_sc = 0
    poczatek_nc = koniec_nc = 0
    najw_suma = ciag[poczatek_nc]
    suma_sc = 0  # suma sprawdzanego ciągu
    for koniec_sc in range(1, len(ciag)):
        if ciag[koniec_sc] >= ciag[koniec_sc - 1]:  # mamy ciąg niemalejący
            suma_sc += ciag[koniec_sc]
            if suma_sc > najw_suma:
                najw_suma = suma_sc
                print(poczatek_nc, koniec_nc, suma_sc)
                koniec_nc = koniec_sc
                poczatek_nc = poczatek_sc
        else:  # koniec ciągu niemalejącego, zaczynamy nowy ciąg
            poczatek_sc = koniec_sc
            suma_sc = ciag[koniec_sc]
    return poczatek_nc, koniec_nc, najw_suma

def znajdz_npnm_suma_dl(ciag, m):
    """Znajdowanie spójnego podciągu o zadanej długości i największej sumie"""
    poczatek_sc = 0
    poczatek_nc = koniec_nc = 0
    najw_suma = ciag[poczatek_nc]
    suma_sc = 0  # suma sprawdzanego ciągu
    for koniec_sc in range(1, len(ciag)):
        if ciag[koniec_sc] >= ciag[koniec_sc - 1]:  # mamy ciąg niemalejący
            suma_sc += ciag[koniec_sc]
            if suma_sc > najw_suma:
                najw_suma = suma_sc
                print(poczatek_nc, koniec_nc, suma_sc)
                koniec_nc = koniec_sc
                poczatek_nc = poczatek_sc
        else:  # koniec ciągu niemalejącego, zaczynamy nowy ciąg
            poczatek_sc = koniec_sc
            suma_sc = ciag[koniec_sc]
    return poczatek_nc, koniec_nc, najw_suma

dane = (23, 6, 7, 9, 11, 5, 90, 1, 35, 100)
indeks_p, indeks_k = znajdz_npnm(dane)
print(indeks_p, indeks_k)
print(dane[indeks_p:indeks_k + 1])

indeks_p, indeks_k, najw_suma = znajdz_npnm_suma(dane)
print(indeks_p, indeks_k, najw_suma)
print(dane[indeks_p:indeks_k + 1])