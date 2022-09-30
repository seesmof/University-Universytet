#include <iostream>
#include <math.h>

using namespace std;

int main(int argc, char **argv)
{
    int a;
    double f;

    cout << "Enter A number: " << endl;
    cin >> a;

    if (a <= 2)
    {
        f = pow(a, 2) + 4 * a + 5;
    }
    else
    {
        f = 1 / (pow(a, 2) + 4 * a + 5);
    }

    cout << "The result is " << f << endl;

    return 0;
}

// 1.3.2.23 б)