/*
 * bmi.cpp
 */
using namespace std;

#include <iostream>

void pobierzDane(float &m, float &w) {
    cout << "Podaj masę ciała (kg): ";
    cin >> m;
    while (m < 10 || m > 200) {
        cout << "Błędna wartość" << endl;
        cout << "Podaj masę ciała (kg): ";
        cin >> m;
    }
    cout << "Podaj wzrost (m): ";
    cin >> w;
    while (w < 1 || w > 2.5) {
        cout << "Błędna wartość" << endl;
        cout << "Podaj wzrost (m): ";
        cin >> w;
    }
}

float obliczBmi(float m, float w) {
    float bmi = m / (w * w);
    return bmi;
}

void wydrukujDiagnoze(float bmi) {
    if (bmi < 18.5) {
        cout << "niedowaga";
    } else if (bmi < 25) {
        cout << "norma";
    } else if (bmi < 30) {
        cout << "nadwaga";
    } else {
        cout << "otyłość";
    }
}

int main(int argc, char **argv)
{
    // deklaracja zmiennych, może zawierać inicjację wartości zmiennej
    // deklarcja + inicjacja = definicja
    float m = 0;
    float w = 0;
    float bmi = 0;

    pobierzDane(m, w);
    bmi = obliczBmi(m, w);
    cout << bmi << endl;
    wydrukujDiagnoze(bmi);

	return 0;
}

