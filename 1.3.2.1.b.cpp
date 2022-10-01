#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <iostream>

using namespace std;

int main(int argc, char **argv)
{
    double a, b, c;

    cout << "Enter A: " << endl;
    cin >> a;

    cout << "Enter B: " << endl;
    cin >> b;

    cout << "Enter C: " << endl;
    cin >> c;

    if (b >= a && b <= c)
    {
        a = a / 2;
        b = b / 2;
        c = c / 2;

        cout << a << " " << b << " " << c << endl;
    }
    else
    {
        a = abs(a);
        b = abs(b);
        c = abs(c);

        cout << a << " " << b << " " << c << endl;
    }

    return 0;
}