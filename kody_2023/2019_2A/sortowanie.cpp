/*
 * sortowanie.cpp
 */
#include <iostream>
using namespace std;

void wypelnij(int tab[], int n) {
    srand(time(NULL));
    for (int i=0; i<n; i++) {
        tab[i] = rand() % n;
    }
}

void wyswietl(int tab[], int n) {
    for (int i=0; i<n; i++) {
        cout << tab[i] << " ";
    }
    cout << endl;
}

void copytab(int tab[], int tab2[], int n) {
    for (int i=0; i<n; i++) {
        tab2[i] = tab[i];
    }
}

void insert_sort(int tab[], int n) {
    int i, k, el;
    for(i=1; i<n; i++) {
        el = tab[i];
        k = i - 1;
        while (k>=0 && tab[k] < el) {
            tab[k+1]=tab[k];
            k--;
        }
        tab[k+1]=el;
    }
}

void zamien(int &a, int &b) {
    int tmp=a;
    a = b;
    b = tmp;
}

// sortowanie przez wybór
void selection_sort(int tab[], int n) {
    int ile = 0;
    int i, j, k;
    for(i=0; i<n; i++) {
        k = i;
        for (j=i+1; j<n; j++) {
            if (tab[j]<tab[k])
                k=j;
        }
        zamien(tab[k], tab[i]);
        ile++;
    }
    cout << "Zamian: " << ile << endl;
}

// 5, 3, 8, 5, 1, 0, 9
// 3, 5, 5, 1, 0, 8, 9
// 3, 5, 1, 0, 5, 8, 9

dla n liczb = n-1, n-2 n-3, n-..., 1
S(k) = (a1 + ak) / 2 * k
a1 = 1
ak = n-1
k = n - 1

Ln = Sk = (1 + n-1) / 2 * (n-1)= n / 2 * (n-1) = n^2 - n / 2
O(n^2)

// sortowanie bąbelkowe
void bubble_sort(int tab[], int n) {
    int ile = 0;
    for (int i=n-1; i > 0; i--) {
        cout << "Indeks i=" << i << endl;
        for (int j=0; j < i; j++) {
            cout << "Indeks j=" << j << " ";
            if (tab[j] < tab[j+1]) {
                zamien(tab[j], tab[j+1]);
                ile++;
            }
        }
        cout << endl;
    }
    cout << "Zamian: " << ile << endl;
}


int main(int argc, char **argv) {
	int tab1[50];
    int tab2[50];
    int n;
    cout << "Ile elementów ma zawierać tablica (max=50)? ";
    cin >> n;
    wypelnij(tab1,n);
    copytab(tab1, tab2, n);
    wyswietl(tab2, n);
    selection_sort(tab1, n);
    bubble_sort(tab2, n);
    wyswietl(tab1, n);
    
	return 0;
}

