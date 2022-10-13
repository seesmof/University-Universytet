#include <iostream>
#include <math.h>
#include <cmath>

using namespace std;

int main(int argc, char **argv)
{
    int a, a1, a2, a3;

    cout << "Enter the number: " << endl;
    cin >> a;

    a1 = a * a;
    // 2 ступінь
    a2 = a * a1;
    // 3 ступінь
    a3 = a1 * a2;
    // 5 ступінь

    cout << "Your number to the power of 5 = " << a3 << endl;

    return 0;
} // 1.3.2.22 a)