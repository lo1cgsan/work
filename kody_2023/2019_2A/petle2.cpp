/*
 * petle2.cpp
 * 
 * 
 */


#include <iostream>
#include <iomanip>

using namespace std;

void drukujTabliczke(int x, int y) {
    int i, j;
    for (i = 1; i <= x; i++) {
        for (j = 1; j <= y; j++) {
            cout << setw(4) << i * j << " ";
        }
        cout << endl;
    }    
}

void pustak(int x, int y, char z) {
    int i, j;
    for (i = 1; i <= x; i++) {
        for (j = 1; j <= y; j++) {
            if (i == 1 || i == x)
                cout << z;
            else if (j == 1 || j == y)
                cout << z;
            else
                cout << " ";
        }
        cout << endl;
    }    
}


int main(int argc, char **argv)
{
    // drukujTabliczke(5, 10);
    int a, b;
    char znak;
    cout << "Podaj rozmiar x, y: ";
    cin >> a >> b;
    cout << "Podaj znak: ";
    cin >> znak;
    pustak(a, b, znak);
	return 0;
}

