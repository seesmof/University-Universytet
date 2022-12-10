#include <bits/stdc++.h>
using namespace std;

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int A;
        int a, b;
        cin >> a >> b;
        a /= 2;
        b /= 2;
        if (a > b)
            A = a;
        else
            A = b;
        cout << A << endl;
    }
    return 0;
}