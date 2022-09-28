#include <iostream>
#include <cmath>
#include <math.h>
using namespace std;

// FIXME: this doesn't work
int main(int argc, char **argv)
{
    int x;
    int z = pow(3, asin(int(x)));
    int result;

    double pi = 2 * acos(0.0);

    cout << "Enter x: " << endl;
    cin >> x;

    if (z > 0.5)
    {
        result = (pow(2, 2 * z + 1)) / (2.75 - pow(2, x));
    }
    else if (z >= -0.5 && z <= 0.001)
    {
        result = pow(3, sin(z)) - sin(z / 3 * double(pi));
    }
    else if (z > 0.001)
    {
        result = (tan(z + x) - exp(x)) / (3.5 * x);
    }

    cout << "Result is: " << result << endl;

    return 0;
}