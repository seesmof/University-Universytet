#include "../lib.h"

int main()
{
    short n = 0;
    cout << "Loop: 0";
    while (n < 5, ++n)
        cout << n << " ";
    cout << "N = " << n;

    return 0;
}
