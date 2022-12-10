// add necessary libraries
#include <bits/stdc++.h>
using namespace std;

// declare function for calculating the binary of decimal
void decimalToBin(int n)
{
    // declare a local array for storing the result
    int binArr[32];
    // declare a counter
    int i = 0;
    // create a function to calculate the binary
    while (n > 0)
    {
        binArr[i] = n % 2;
        n = n / 2;
        i++;
    }
    // output the result
    for (int s = i - 1; s >= 0; s--)
        cout << binArr[s];
    cout << endl;
}

// declare main function
int main()
{
    cout << endl
         << "/////////////////////////////////////////////////////////////" << endl
         << endl;

    // declare a local variable for storing the input
    int n;
    // ask user to input the number he wants to convert
    cout << "Enter a number you want to convert to binary: ";
    cin >> n;
    // call a function to convert the number to binary
    cout << "The " << n << " in binary is ";
    decimalToBin(n);

    cout << endl
         << "/////////////////////////////////////////////////////////////" << endl
         << endl;
    //  end main function
    return 0;
}