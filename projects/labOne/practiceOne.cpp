#include <iostream>
#include <math.h>

using namespace std;

int main(int argc, char **argv)
{
    int i, n;
    double v = 0.0;

    cout << "Enter the number: " << endl;
    cin >> n;

    for (i = n; i >= 1; i--)
    {
        v = pow(5 * i + v, 1.0 / i);
        cout << v << endl;
    }

    return 0;
}