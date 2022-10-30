#include <iostream>

using namespace std;

int main(int argc, char **argv)
{
    double sum = 0.0;
    for (int m = 1; m <= 10; m++)
    {
        for (int n = 0; n <= m; n++)
        {
            sum += 1.0 / (2 * n + 3 * m);
        }
    }
    cout << "Sum = " << sum << endl;

    return 0;
}