#include <iostream>
#include <math.h>

using namespace std;

int main(int argc, char **argv)
{
    double sum = 0.0, x, t, e = 0.0001;
    int i = 1, d = 1, f = 1;

    cout << "Enter X: " << endl;
    cin >> x;

    do
    {
        t = d * pow(x, i) / f;
        d *= (-1);
        i += 2;
        f *= (i - 1) * i;
        sum += t;
    } while (fabs(t) > e);
    cout << "Sum = " << sum << endl;

    return 0;
}