/*
 * rekordy.cpp
 */
#include <iostream>
#include <fstream>
#include <cstring>

using namespace std;

struct uczen{
    char imie[10];
    char nazwisko[20];
    float srednia;
};

void pobierzDane(uczen tab[], int ilu) {
    uczen *wsk;
    wsk = tab;
    for (int i=0; i<ilu; i++) {
        cout << "Imię: "; cin >> wsk->imie;
        cout << "Nazwisko: "; cin >> wsk->nazwisko;
        cout << "Średnia: "; cin >> wsk->srednia;
        cout << wsk << endl;
        wsk++;
    }
}

void drukujDane(uczen tab[], int ilu) {
    uczen *wsk;
    wsk = tab;
    for (int i=0; i<ilu; i++) {
        cout << "Imię: "; cout << wsk->imie << endl;
        cout << "Nazwisko: "; cout << wsk->nazwisko << endl;
        cout << "Średnia: "; cout << wsk->srednia << endl;
        wsk++;
    }
}

int zapiszDane(uczen tab[], int ilu) {
    uczen *wsk;
    wsk = tab;

    char nazwa[15];
    cout << "Nazwa pliku: ";
    cin >> nazwa;
    ofstream fh(nazwa);
    
    if (!fh) { cout << "Błąd otwarcia pliku!"; return 1; }
    for (int i=0; i<ilu; i++) {
        fh << wsk->imie << endl;
        fh << wsk->nazwisko << endl;
        fh << wsk->srednia << endl;
        wsk++;
    }
    fh.close();
    return 1;
}

int czytajDane(const char *nazwa) {
    ifstream fh(nazwa);
    if (!fh) { cout << "Błąd otwarcia pliku!"; return 1; }
    char linia[20];
    while (!fh.eof()) {
        fh.getline(linia, sizeof(linia));
        cout << linia << endl;
    }
    return 1;
}

int main(int argc, char **argv)
{
    //~int ilu = 0;
    //~cout << "Ilu podasz uczniów: ";
    //~cin >> ilu;
    //~uczen *tab = NULL;
    //~tab = new uczen[ilu];
    //~pobierzDane(tab, ilu);
    //~drukujDane(tab, ilu);
    //~zapiszDane(tab, ilu);
    czytajDane("dane.txt");
    return 0;
}

