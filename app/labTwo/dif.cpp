// include necessary libraries
#include <iostream>
#include <math.h>
using namespace std;

// declare main function
int main(int argc, char **argv)
{
    cout << endl;
    cout << "************************************ Task D ************************************" << endl
         << endl;
    // declare variables
    double sum = 0.0, x, s, e;
    int p = 2, f = 2, nf, sign = -1;

    // ask user to input number of times he wants a program to run
    cout << "Enter accuracy E: ";
    cin >> e;

    // ask user to input number X
    cout << "Enter number X: ";
    cin >> x;

    // create do while loop for calculating the sum
    do
    {
        // create a step
        s = sign * (pow((2 * x), p) / f);

        // create a for loop for calculating factorial
        for (int j = 1; j <= nf; j++)
        {
            f = f * nf;
        }

        // add increments
        p += 2;
        nf += 2;
        sign *= -1;
        sum += s;
    } while (fabs(s) < e);

    // output result
    cout << endl;
    cout << "The sum is " << sum << endl;

    cout << endl;
    cout << "********************************************************************************" << endl
         << endl;

    // end main function
    return 0;
}
