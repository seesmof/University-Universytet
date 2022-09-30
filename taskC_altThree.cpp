#include <iostream>
#include <math.h>

using namespace std;

int main(int argc, char **argv)
{
    int x, y, z;
    double m, p;

    cout << "Enter x, y, z values: " << endl;
    cin >> x >> y >> z;

    m = (1 - pow(sin(x + y), 2)) / (1 + abs((2 * x) / (1 + pow(x, 2) * pow(y, 2)))) - y;
    p = cos(atan(1 / z)) + sin(atan(z));

    cout << "The result is: " << endl;
    cout << m << endl;
    cout << p << endl;

    return 0;
}

// 1.3.2.23 а)