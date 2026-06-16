def znajdz_najdluzszy_niemalejacy(ciag):
    poczatek_n = koniec_n = 0
    poczatek_spr_c = 0
    for koniec_spr_c in range(1, len(ciag)):
        if ciag[koniec_spr_c] >= ciag[koniec_spr_c-1]:
            if koniec_spr_c - poczatek_spr_c > koniec_n - poczatek_n:
                koniec_n = koniec_spr_c
                poczatek_n = poczatek_spr_c
        else:
            poczatek_spr_c = koniec_spr_c
    return poczatek_n, koniec_n

ciag = (23, 6, 7, 7, 9, 11, 5, 90, 1, 35, 100)
p, k = znajdz_najdluzszy_niemalejacy(ciag)
print(p, k)
