/*
 * typydanych.cpp
 * 
 */

#include <iostream>
#include <fstream>

using namespace std;

// typ wyliczeniowy
enum REZULTAT {
    ISTNIEJE = 1,
    NIEISTNIEJE = -1
};

REZULTAT czyjest(const char *npliku) {
    ifstream f(npliku);
    if (f.good()) {
        f.close();
        return ISTNIEJE;
    } else {
        f.close();
        return NIEISTNIEJE;
    }
}

#define ROZMIAR 20

void testtyp() {
    char plik[ROZMIAR];
    cout << "Podaj nazę pliku: ";
    cin.getline(plik, ROZMIAR);
    
    REZULTAT jestplik = czyjest(plik);
    if (jestplik == ISTNIEJE) {
        cout << "Plik jest na dysku\n";
    } else if (jestplik == NIEISTNIEJE) {
        cout << "Pliku nie ma\n";
    }
}

int main(int argc, char **argv)
{
	testtyp();
	return 0;
}

