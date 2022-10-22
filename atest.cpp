#include <iostream>
#include <math.h>

using namespace std;

int main(int argc, char **argv)
{
    int n;
    cin >> n;
    cout << "The divisors are " << 1 << " " << n << " ";
    for (int d = 2; d <= (n / 2); d++)
    {
        if (n % d == 0)
        {
            cout << d << " ";
        }
    }
    return 0;
}