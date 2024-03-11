/*
 * tablica.cpp
 * 
 * Copyright 2019  <>
 * 
 */


#include <iostream>
using namespace std;

void pobierzOceny(int t[], int r) {
    cout << "Podaj " << r << " ocen: " << endl;
    int i;
    for (i=0; i < r; i++) {
        cin >> t[i];
    }
}

void drukujTab(int t[], int r) {
    int i;
    for (i=0; i < r; i++) {
        cout << t[i];
    }
}

int main(int argc, char **argv)
{
    cout << "Ile ocen podasz? ";
    int rozmiar;
    cin >> rozmiar;
    int tablica[rozmiar];

    pobierzOceny(tablica, rozmiar);
    drukujTab(tablica, rozmiar);

    return 0;
}

