#include "D:\repos\university\lib.h"

template <typename T>
T _max(T a, T b)
{
    return a > b ? a : b;
}

int main()
{
    ll a, b;
    cin >> a >> b;
    cout << _max(a, b);
    double c, d;
    cin >> c >> d;
    cout << _max(c, d);
}