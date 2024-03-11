/*
 * zlozonosc.cpp
  */


#include <iostream>
using namespace std;

// Ln = 1
// Ln = n
// O(n)

int main(int argc, char **argv)
{
    int n = 5;
    int tb[n] = {3, 5, 8, 1, 9};
    int i = 0;
    int x = 9;
    for (i = 0; i < n; i++) {
        if (tb[i] == x) {
            cout << i;
            return 0;
        }
    }
    cout << -1;
    return 0;
}
