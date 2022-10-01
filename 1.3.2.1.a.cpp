#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <iostream>

using namespace std;

int main(int argc, char **argv)
{
    double f1, f2, x, x1, x2, x3, x4, x5, x6, x7, x8, x9;

    x1 = x * x;
    // 2
    x2 = x1 * x;
    // 3
    x3 = x2 * x1;
    // 5
    x4 = x3 * x2;
    // 8

    cout << "Enter X: " << endl;
    cin >> x;

    f1 = 13 * x2 * x + 7 * x2 + 6 * x + 5;
    f2 = 7 * x2 - 13 * x2 * x - 6 * x + 5;

    cout << "First answer is: " << f1 << endl;
    cout << "Second answer is: " << f2 << endl;

    return 0;
}