#include <bits/stdc++.h>
using namespace std;

int main()
{
    enum shape
    {
        Circle,
        Square,
        Triangle
    };
    shape out;
    int in;
    cout << "Enter a shape: ";
    cin >> in;
    switch (in)
    {
    case 0:
    {
        cout << "Circle" << endl;
        break;
    }
    case 1:
    {
        cout << "Square" << endl;
        break;
    }
    case 2:
    {
        cout << "Triangle" << endl;
        break;
    }
    }

    return 0;
}