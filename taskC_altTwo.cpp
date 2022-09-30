#include <iostream>
#include <cmath>
#include <math.h>

using namespace std;

int main(int argc, char **argv)
{
    int x, y;
    double m;

    cout << "Enter the number X: " << endl;
    cin >> x;

    cout << "Enter the number Y: " << endl;
    cin >> y;

    m = (pow(x, 2) + 1.3 * x + 0.37) / (cos(2 * y) + 7.1);
    cout << "The result is " << m << endl;

    return 0;
}

// 1.3.2.12 г)