/*
 * drzewo_bin.cpp
 */
#include <iostream>
using namespace std;

struct WEZEL {
    int wartosc;
    WEZEL* lewy;
    WEZEL* prawy;
} *korzen = NULL;

WEZEL* stworzWezel(int wartosc) {
    WEZEL* nowyWezel = new WEZEL;
    nowyWezel->wartosc = wartosc;
    nowyWezel->lewy = NULL;
    nowyWezel->prawy = NULL;
    return nowyWezel;
}

void dodajWezel(WEZEL* wezel, int wartosc) {
    if (korzen == NULL) {
        korzen = stworzWezel(wartosc);
    } else {
        if (wartosc < wezel->wartosc) { // wstawiamy do lewego poddrzewa
            if (wezel->lewy != NULL) {
                dodajWezel(wezel->lewy, wartosc);
            } else {
                wezel->lewy = stworzWezel(wartosc);
            }
        } else { // wstawiamy do prawego poddrzewa
            if (wezel->prawy != NULL) {
                dodajWezel(wezel->prawy, wartosc);
            } else {
                wezel->prawy = stworzWezel(wartosc);
            }
        }
    }
}

void wyswietlRosnaco(WEZEL *wezel) {
    if (wezel != NULL) {
        // rekurencyjne wyswietlanie lewego poddrzewa
        wyswietlRosnaco(wezel->lewy);
        cout << wezel->wartosc << ", ";
        // rekurencyjne wyswietlanie prawego poddrzewa
        wyswietlRosnaco(wezel->prawy);
    }
}

void wyswietlMalejaco(WEZEL *wezel) {
    ;
}

void usunWezel(WEZEL* wezel, int wartosc) {
    ;
}

int main(int argc, char **argv)
{
    dodajWezel(korzen, 8);
    dodajWezel(korzen, 3);
    dodajWezel(korzen, 10);
    dodajWezel(korzen, 1);
    dodajWezel(korzen, 6);
    dodajWezel(korzen, 14);
    cout << "Drzewo posortowane niemalejąco:" << endl;
    wyswietlRosnaco(korzen);
    wyswietlMalejaco(korzen);
    usunWezel(korzen, 6);
    return 0;
}

