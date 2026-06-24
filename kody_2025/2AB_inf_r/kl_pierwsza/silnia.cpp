#include <iostream>

using namespace std;

int main(int argc, char **argv)
{
    int n;
    cout << "Podaj n: ";
    cin >> n;

    long int silnia = 1;

    for (int i=1; i<n+1; i++) {
        silnia = silnia * i;
    }

    cout << silnia << endl;
    return 0;
}
