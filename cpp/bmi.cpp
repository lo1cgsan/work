/*
 * bmi.cpp
 */

using namespace std;

#include <iostream>

int main(int argc, char **argv)
{
    // deklaracja zmiennych, może zawierać inicjację wartości zmiennej
    // deklarcja + inicjacja = definicja
    float m = 0;
    float w = 0;
    float bmi = 0;
    
    cout << "Podaj masę ciała (kg): ";
    cin >> m;

    cout << "Podaj wzrost (m): ";
    cin >> w;

    cout << m << " " << w << endl;
    
    bmi = m / (w * w);
    cout << bmi << endl;

    if (bmi < 18.5) {
        cout << "niedowaga";
    } else if (bmi < 25) {
        cout << "norma";
    } else if (bmi < 30) {
        cout << "nadwaga";
    } else {
        cout << "otyłość";
    }

	return 0;
}

