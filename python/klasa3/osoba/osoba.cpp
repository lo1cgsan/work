#include <iostream>
#include <cstdlib>
#include "osoba.h"

Osoba::Osoba() {
    imie = nazwisko = plec = "";
    wiek = 0;
}

Osoba::Osoba(string i, string n, int w, string p) {
    imie = i;
    nazwisko = n;
    if (w > 0) wiek = w;
    else w = 0;
    plec = p; 
}
