/*
 * szukaj_bin.cpp
 */
#include <iostream>
using namespace std;

void wypelnij(int tab[], int roz) {
    srand(time(NULL));
    for(int i=0; i < roz; i++) {
        tab[i] = rand() % 101;
    }
}

void drukuj(int tab[], int roz) {
    for(int i=0; i < roz; i++) {
        cout << tab[i] << " ";
    }
    cout << endl;
}

void zamien(int &a, int &b) {
    int tmp = a;
    a = b;
    b = tmp;
}

void sort_bubble(int tab[], int n) {
    for (int j = n-1; j > 0; j--) {
        for (int i = 0; i < j; i++) {
            if (tab[i] > tab[i+1])
                zamien(tab[i], tab[i+1]);
        }
    }
}

int szukaj_bin_rek(int t[], int p, int k, int szukany) {
    // p = 0
    // k = n-1
    if (p<=k) {
        int s = (p + k) / 2;
        if (t[s] == szukany) return s;
        if (t[s] > szukany) {
            return szukaj_bin_rek(t, p, s-1, szukany);
        } else {
            return szukaj_bin_rek(t, s+1, k, szukany);
        }
    }
    return -1;

/*
    if (p<=k) {
        int s = (p + k) / 2;
        if (t[s] == szukany) return s;
        else if (t[s] > szukany) {
            szukaj_bin_rek(t, p, s-1, szukany);
        } else {
            szukaj_bin_rek(t, s+1, k, szukany);
        }
    } else return -1;
*/

}

int main(int argc, char **argv)
{
	int n, szukany;
    cout << "Podaj ilość liczb: ";
    cin >> n;
    int t[n];
    wypelnij(t, n);
    sort_bubble(t, n);
    drukuj(t, n);
    cout << "Podaj szukaną liczbę: ";
    cin >> szukany;
    cout << szukaj_bin_rek(t, 0, n-1, szukany);
	return 0;
}

