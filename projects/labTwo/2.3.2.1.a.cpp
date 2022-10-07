#include <iostream>
#include <math.h>

using namespace std;

int main(int argc, char **argv)
{
    double sum = 0.0, x, t = 1, e = 0.0001;
    int i, d, f;

    cout << "Enter X: " << endl;
    cin >> x;

    for (i = 1, d = 1, f = 1; fabs(t) > e; i += 2)
    {
        if (i > 1)
        {
            f *= (i - 1) * i;
            d *= (-1);
        }
        t = d * pow(x, i) / f;

        sum += t;
    }

    cout << "Sum = " << sum << endl;

    return 0;
}