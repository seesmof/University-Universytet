#include <iostream>
#include <math.h>

using namespace std;

int main(int argc, char **argv)
{
    double a, b, c;

    cout << "Enter number A: " << endl;
    cin >> a;
    cout << "Enter number B: " << endl;
    cin >> b;
    cout << "Enter number C: " << endl;
    cin >> c;

    if (a <= b && b <= c)
    {
        cout << "A = " << a / 2 << endl;
        cout << "B = " << b / 2 << endl;
        cout << "C = " << c / 2 << endl;
    }
    else
    {
        cout << "A = " << abs(a) << endl;
        cout << "B = " << abs(b) << endl;
        cout << "C = " << abs(c) << endl;
    }

    return 0;
}

// 1.3.2.1 б)