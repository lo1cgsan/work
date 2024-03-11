/*
 * sumuj.cpp
 * Program sumujący dwie liczby całkowite
 * i drukujący wynik w terminalu.
 */

#include <iostream>
using namespace std;

int main(int argc, char **argv)
{
    long long a, b;
    a = b = 0;
    cout << "Podaj dwie liczby: ";
    cin >> a >> b;
    cout << "Suma: " << a + b << endl;
    return 0;
}

