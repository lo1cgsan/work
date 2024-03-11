/*
 * petla.cpp
 */


#include <iostream>

using namespace std;

int main(int argc, char **argv)
{
    int i = 0;
	for(i = 0; i <= 20; i += 2) {
        cout << i << endl;
        cout << "Hello!";
    }
    
    cout << endl << "Wartość i: " << i << endl;
	return 0;
}
