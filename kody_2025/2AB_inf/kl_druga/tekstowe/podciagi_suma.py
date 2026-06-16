def znajdz_najwiekszy_niemalejacy(ciag):
    poczatek_n = koniec_n = 0
    poczatek_spr_c = 0
    suma_n = ciag[0]
    suma_spr_c = suma_n
    for koniec_spr_c in range(1, len(ciag)):
        print(ciag[koniec_spr_c], ciag[koniec_spr_c-1])
        if ciag[koniec_spr_c] >= ciag[koniec_spr_c-1]:
            suma_spr_c += ciag[koniec_spr_c]
            if suma_spr_c > suma_n:
                koniec_n = koniec_spr_c
                poczatek_n = poczatek_spr_c
                suma_n = suma_spr_c
        else:
            poczatek_spr_c = koniec_spr_c
            suma_spr_c = ciag[koniec_spr_c]
    return poczatek_n, koniec_n, suma_n

ciag = (23, 6, 7, 7, 9, 156, 5, 90, 1, 35, 100)
p, k, s = znajdz_najwiekszy_niemalejacy(ciag)
print(p, k, s)
