/*
 * znaki.cpp
 * znakiem kończącycm tablicę znakową jest \0
 */


#include <iostream>

using namespace std;


void ascii() {
    int i = 0;
    for (i = 65; i < 91; i++) {
        cout << i << " - " << char(i) << endl;
    }
}


void litery2liczby(char tabzn[], int rozmiar) {
    for (int i = 0; i < rozmiar; i++) {
        cout << tabzn[0] << " - " << (int)tabzn[i] << endl;
    }
}

void koduj(char tabzn, int rozmiar) {
    char tab[] = "123\231";
    cout << tab;
}

void dekoduj(int tabliczb; rozmiar) {
    ;
}

int main(int argc, char **argv)
{
    int rozmiar = 11;
    char tekst[rozmiar] = "Ala ma kota!";
    koduj(tekst, rozmiar);
//    int szyfr[11] = {65, 78, 90};
//   dekoduj(szyfr, rozmiar);
    
//    ascii();
//    litery2liczby(napis, rozmiar);
    
    return 0;
}

