#include <iostream>
#include <math.h>

using namespace std;

int main(int argc, char **argv)
{
    double sum = 0.0, x, n, t;
    int i = 1, f = 1;

    cout << "Enter X: " << endl;
    cin >> x;
    cout << "Enter N: " << endl;
    cin >> n;

    do
    {
        t = pow(x, i) / f;
        i += 1;
        f *= (i - 1) * i;
        sum += t;
    } while (i <= n);
    cout << "Sum = " << sum << endl;

    return 0;
}