#include <iostream>
#include <cmath>
using namespace std;

int main()
{
    int n, m;
    cin >> n >> m;
    int **a;
    a = new int *[n];
    for (int i = 0; i < n; i++)
        a[i] = new int[m];
    for (int i = 0; i < n; i++)
        for (int j = 0; i < m; j++)
            cin >> a[i][j];
    for (int i = 0; i < m; i++)
    {
        for (int j = 0; j < m; j++)
            cout << a[i][j] << " ";
        cout << endl;
    }
    for (int i = 0; i < n; i++)
        delete[] a[i];
    delete[] a;
    return 0;
}