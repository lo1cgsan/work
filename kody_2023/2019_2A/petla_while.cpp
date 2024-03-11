/*
 * petla_while.cpp
 */


#include <iostream>

using namespace std;

int main(int argc, char **argv)
{
    int i = 0; // DEKLARACJA i INICJACJA = DEFINICJA
	while(i <= 20) {
        cout << i << endl;
        cout << "Hello!";
        i += 2;
    }
    
    cout << endl << "Wartość i: " << i << endl;
	return 0;
}
