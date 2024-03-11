/*
 * uczniowie.cpp
 */
#include <iostream>
#include <fstream>

using namespace std;

struct uczen {
    char imie[10];
    char nazwisko[30];
    float srednia;
};

void pobierzDane(uczen tab[], int ilu) {
    uczen *wsk = NULL;
    wsk = tab;
    for(int i=0; i<ilu; i++) {
        cout << "Imię: ";
        cin >> wsk->imie;
        cout << "Nazwisko: ";
        cin >> wsk->nazwisko;
        cout << "Średnia: ";
        cin >> wsk->srednia;
        wsk++;
    }
}

void drukujDane(uczen tab[], int ilu) {
    uczen *wsk = NULL;
    wsk = tab;
    for(int i=0; i<ilu; i++) {
        cout << "Imię: " << wsk->imie << endl;
        cout << "Nazwisko: " << wsk->nazwisko << endl;
        cout << "Średnia: " << wsk->srednia << endl;
        cout << endl;
        wsk++;
    }
}

int zapiszDane(uczen tab[], int ilu) {
    uczen *wsk = NULL;
    wsk = tab;
    char nazwa[15];
    cout << "Podaj nazwę pliku z rozserzeniem .txt: ";
    cin.getline(nazwa, 15);
    ofstream wf(nazwa);
    if (!wf) { cout << "Błąd otwarcia pliku!"; return 1; }
    for(int i=0; i<ilu; i++) {
        wf << wsk->imie << endl;
        wf << wsk->nazwisko << endl;
        wf << wsk->srednia << endl;
        wsk++;
    }
    wf.close();
    return 0;
}

int main(int argc, char **argv) {
	int ilu;
    cout << "Ilu podasz uczniów? " << endl;
    cin >> ilu;
    uczen *tab = NULL;
    tab = new uczen[ilu];
    pobierzDane(tab, ilu);
    drukujDane(tab, ilu);
    zapiszDane(tab, ilu);
	return 0;
}

