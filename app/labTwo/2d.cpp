#include <iostream>
#include <math.h>

using namespace std;

int main(int argc, char **argv)
{
    double sum = 0.0, x, e, s, nf;
    int f = 2, i = 2;

    cout << "Enter X: ";
    cin >> x;
    cout << "Enter E: ";
    cin >> e;

    do
    {
        s = pow(x, i) / f;
        for (int j = 1; j <= nf; j++)
        {
            f = f * nf;
        }
        nf += 2;
        i += 2;
        sum += s;
    } while (fabs(s) > e);

    cout << "The sum is " << sum << endl;
    return 0;
}