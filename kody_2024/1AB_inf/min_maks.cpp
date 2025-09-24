#include <iostream>
#include <cstdlib>

using namespace std;
const int N = 10;

void losuj_liczby(int tab[N]) {
    srand(time(NULL));
    for (int i=0; i<N; i++) {
        tab[i] = rand()%100;
    }
}

void wypisz_liczby(int tab[N]) {
    for (int i=0; i<N; i++) {
        cout << tab[i] << "\n";
    }
}

int main() {
    int liczby[N];
    losuj_liczby(liczby);
    wypisz_liczby(liczby);
    return 0;
}
