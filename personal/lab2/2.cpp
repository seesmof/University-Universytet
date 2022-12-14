// include necessary libraries
#include <bits/stdc++.h>
using namespace std;

// declare main function
int main()
{
    // project intro
    cout << endl
         << "/////////////////////////////////////////////////////////////" << endl
         << endl
         << "Welcome! This program will calculate a double sum" << endl
         << endl
         << "/////////////////////////////////////////////////////////////" << endl
         << endl;
    char doContinue;
    do
    {
        //////////////////////////////////////////////////////////////////////////////////
        long long int M, N;
        cout << "Enter M: ";
        cin >> M;
        cout << "Enter N: ";
        cin >> N;

        long long int sum = 0;
        for (long long int m = 1; m <= M; m++)
        {
            for (long long int n = 1; n <= N; n++)
            {
                sum += (1 / (m * n));
            }
        }

        cout << "Sum: " << sum;
        //////////////////////////////////////////////////////////////////////////////////
        cout << endl
             << endl
             << "/////////////////////////////////////////////////////////////" << endl
             << endl
             << "Would you like to continue program execution? (Y | N): ";
        cin >> doContinue;
        if (doContinue == 'N' || doContinue == 'n')
        {
            cout << endl
                 << "Thanks for using this program." << endl
                 << endl
                 << "/////////////////////////////////////////////////////////////" << endl
                 << endl;
            break;
        }
        else
        {
            cout << endl
                 << "/////////////////////////////////////////////////////////////" << endl
                 << endl;
            continue;
        }
    } while (doContinue = 'Y' || doContinue == 'y');

    // end main function
    return 0;
}