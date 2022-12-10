// include necessary libraries
#include <bits/stdc++.h>
using namespace std;

// function prototypes //

/////////////////////////

// declare main function
int main()
{
     // declare local variables //
     srand(time(NULL));
     char doContinue;

     /////////////////////////////

     // project intro
     cout << endl
          << "/////////////////////////////////////////////////////////////" << endl
          << endl
          << "Welcome! This program will " << endl
          << endl
          << "/////////////////////////////////////////////////////////////" << endl
          << endl;
     do
     {
          //////////////////////////////////////////////////////////////////////////////////

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