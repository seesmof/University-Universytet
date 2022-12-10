// include necessary libraries
#include <bits/stdc++.h>
using namespace std;

// create a function that will generate random string
string randString(int ch)
{
     // declare max array length
     const int maxArrSize = 25;
     // declare possible characters
     char possibleCharactersArr[maxArrSize] = {'a', 'b', 'c', 'd', 'e', 'f', 'g',
                                               'h', 'i', 'j', 'k', 'l', 'm', 'n',
                                               'o', 'p', 'q', 'r', 's', 't', 'u',
                                               'v', 'w', 'x', 'y'};
     // declare result string
     string result = "";
     // create for loop
     for (int i = 0; i < ch; i++)
          // add random character from an earlier declared set to the string
          result += possibleCharactersArr[rand() % maxArrSize];

     // return result
     return result;
}

// declare main function
int main()
{
     srand(time(NULL));
     char doContinue;

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
          int t;
          cout << "Execute for: ";
          cin >> t;
          while (t--)
          {
               int holder = rand() % 100;
               string temp = randString(holder);
               cout << temp << endl
                    << endl;
          }
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