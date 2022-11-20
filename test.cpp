// include necessary libraries
#include <iostream>
#include <unistd.h>
#include <string>
using namespace std;

long double factorialCalculator(int);

// declare main function
int main(int argc, char **argv)
{
     // output program intro
     cout << endl;
     cout << "******************************************************************************" << endl
          << endl;

     int k;
     cout << "Enter a number: ";
     cin >> k;
     long double f;
     for (int i = 1; i <= k; i++)
     {
          f = factorialCalculator(i);
          cout << i << "! is " << f << endl;
     }

     // output project outro
     cout << endl;
     cout << "******************************************************************************" << endl
          << endl;

     // end main function
     return 0;
}

long double factorialCalculator(int n)
{
     if (n == 1)
     {
          return 1;
     }
     else
     {
          return factorialCalculator(n - 1) * n;
     }
}