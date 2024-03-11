/*
 * typydanych.cpp
 * 
 */

#include <iostream>
#include <fstream>

using namespace std;

#define ROZMIAR 20

void zapisz_znaki(const char *plik) {
    char znak = ' ';
    ofstream f;
    f.open(plik);
    while(znak != 27) {
        znak = cin.get();
        f << znak;
    }
    f.close();
}

int main(int argc, char **argv)
{
	char plik[ROZMIAR];
    cout << "Podaj nazwę pliku: ";
    cin.getline(plik, ROZMIAR);
    zapisz_znaki(plik);
	return 0;
}

