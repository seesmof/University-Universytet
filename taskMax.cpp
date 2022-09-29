#include <iostream>

using namespace std;

int main(int argc, char **argv)
{
    int x, y, z, max;

    cout << "Enter X: " << endl;
    cin >> x;

    cout << "Enter Y: " << endl;
    cin >> y;

    cout << "Enter Z: " << endl;
    cin >> z;

    if (x > y)
    {
        max = x;
    }
    else
    {
        max = y;
    }

    if (max < z)
    {
        max = z;
    }

    cout << "Max: " << max << endl;
}