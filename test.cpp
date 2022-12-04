#include <bits/stdc++.h>
using namespace std;

int findMinFromArr(int n, vector<int> &v)
{
     if (n == 1)
          return v[0];
     else
          return min(v[n - 1], findMinFromArr(n - 1, v));
}

int main()
{
     srand(time(NULL));
     cout << endl
          << "/////////////////////////////////////////////////////////////" << endl
          << endl;
     ///////////////////////////////////////////////////////////////////////////////
     int n;
     cout << "Enter arr size: ";
     cin >> n;
     vector<int> arr(n);
     cout << endl
          << "Your array is " << endl;
     for (int i = 0; i < n; i++)
     {
          arr[i] = rand() % 100 + 10;
          if (i == 0)
               cout << arr[i];
          else
               cout << setw(4) << arr[i];
     }
     cout << endl;
     cout << endl
          << "Minimal element from array is " << findMinFromArr(n, arr) << endl;
     ///////////////////////////////////////////////////////////////////////////////
     cout << endl
          << "/////////////////////////////////////////////////////////////" << endl
          << endl;
     return 0;
}