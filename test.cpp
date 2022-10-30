#include <iostream>
#include <math.h>
using namespace std;

int main(int argc, char **argv)
{
    int f, n, count = 0;
    double minus = 0.0;
    int *sum = new int[f];
    cout << "Enter array size: ";
    cin >> f;
    for (int i = 0; i < f; i++)
    {
        cout << "Enter element number " << i + 1 << ": ";
        cin >> sum[i];
        if (sum[i] < 0)
        {
            minus += abs(sum[i]);
            count++;
        }
    }
    if (count > 0)
    {
        minus /= count;
        cout << "Average of negatives = " << minus << endl;
    }
    for (int i = 0; i < f; i++)
    {
        if (abs(sum[i]) > minus)
        {
            n += sum[i];
        }
    }
    cout << "Average = " << n << endl;
    if (n < minus)
    {
        cout << "Invalid" << endl;
    }

    return 0;
}