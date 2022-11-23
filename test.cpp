// include necessary libraries
#include <iostream>
#include <unistd.h>
#include <string>
#include <vector>
#include <iomanip>
using namespace std;

void mySwap(int &v1, int &v2)
{
     int temp = v2;
     v2 = v1;
     v1 = temp;
}

// declare main function
int main(int argc, char **argv)
{
     // output program intro
     cout << endl;
     cout << "******************************************************************************" << endl
          << endl;

     int a = 1, b = 2;
     mySwap(a, b);
     cout << a << " " << b << endl;

     // output project outro
     cout << endl;
     cout << "******************************************************************************" << endl
          << endl;

     // end main function
     return 0;
}