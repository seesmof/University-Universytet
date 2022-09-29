#include <iostream>
#include <cmath>
#include <math.h>
using namespace std;

int main(int argc, char **argv)
{
    double x, z, f;
    z = pow(3, asin(x));

    cout << "Enter x: " << endl;
    cin >> x;

    if (z > -0.5)
    {
        f = pow(2, (2 * z + 1)) / 2.75 - pow(2, x);
    }
    else if (z >= -0.5 && z <= 0.001)
    {
        f = pow(3, sin(z)) - sin(z / 3);
    }
    else if (z > 0.001)
    {
        f = (tan(z + x) - exp(x)) / (3.5 * x);
    }

    cout << "The result is: " << f << endl;
}