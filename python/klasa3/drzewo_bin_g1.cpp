/*
 * drzewo_bin_g1.cpp
 */
#include <iostream>
using namespace std;

struct WEZEL {
    int wartosc;
    WEZEL* lewy;
    WEZEL* prawy;
} *korzen = NULL;

WEZEL* stworzWezel(int wartosc) {
    WEZEL *nowyWezel = new WEZEL;
    nowyWezel->wartosc = wartosc;
    nowyWezel->lewy = NULL;
    nowyWezel->prawy = NULL;
    return nowyWezel;
}

void dodajWezel(WEZEL* wezel, int wartosc) {
    if (korzen == NULL) {
        korzen = stworzWezel(wartosc);
    } else {
        if (wartosc < wezel->wartosc) { // lewe poddrzewo
            if (wezel->lewy != NULL) {
                dodajWezel(wezel->lewy, wartosc); // rekurencja
            } else {
                wezel->lewy = stworzWezel(wartosc);
            }
        } else { // prawe poddrzewo
            if (wezel->prawy != NULL) {
                dodajWezel(wezel->prawy, wartosc); // rekurencja
            } else {
                wezel->prawy = stworzWezel(wartosc);
            }
        }
    }
}

void wyswietlRosnaco(WEZEL* wezel) {
    if (wezel != NULL) {
        wyswietlRosnaco(wezel->lewy); // rekurencja
        cout << wezel->wartosc << ", ";
        wyswietlRosnaco(wezel->prawy); // rekurencja
    }
}

int main(int argc, char **argv)
{
	dodajWezel(korzen, 8);
    dodajWezel(korzen, 10);
    dodajWezel(korzen, 2);
    dodajWezel(korzen, 6);
    dodajWezel(korzen, 7);
    dodajWezel(korzen, 90);
    dodajWezel(korzen, 45);
    dodajWezel(korzen, -4);
    cout << "Drzewo posortowane niemalejąco:" << endl;
    wyswietlRosnaco(korzen);
	return 0;
}

