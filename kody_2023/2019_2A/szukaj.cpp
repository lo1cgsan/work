/*
 * szukaj.cpp
 */


#include <iostream>
using namespace std;

int szukaj_it(int liczby[], int ile, int n) {
    int indeks = -1;
    for (int i = 0; i < ile; i++)
        if (liczby[i] == n) return i;

    return indeks;
}


int szukaj_re(int liczby[], int lewy, int prawy, int n) {
    if (lewy > prawy) {
        cout << "Elementu nie znaleziono!" << endl;
        return -1;
    } else {
        if (liczby[lewy] == n) {
            cout << "Element znaleziono!" << endl;
            return lewy;
        } else {
            szukaj_re(liczby, lewy+1, prawy, n);
        }
    }
}


int szukaj_re2(int liczby[], int lewy, int prawy, int n) {
    if (lewy > prawy) {
        cout << "Elementu nie znaleziono!" << endl;
        return -1;
    } else {
        if (liczby[lewy] == n) {
            cout << "Element znaleziono!" << endl;
            return lewy;
        } else {
            szukaj_re(liczby, lewy+1, prawy, n);
        }
    }
}


int main(int argc, char **argv)
{
	int liczby[] = {3, 8, 3, 9, 10, 45, 37};
    int n;
    cout << "Podaj szukany element: " << endl;
    cin >> n;
    // int indeks = szukaj_it(liczby, 7, n);
    int indeks = szukaj_re(liczby, 0, 6, n);
    if (indeks > -1) {
        cout << liczby[indeks] << endl;
    }
    return 0;
}

