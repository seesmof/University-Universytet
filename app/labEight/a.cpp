#include <bits/stdc++.h>
using namespace std;

string fileNameInput()
{
     bool isExtensionFound = false;
     string input;

     cout << "Enter the name of the file: ";
     cin >> input;
     cin.ignore();

     for (int i = 0; i < input.length(); i++)
     {
          if (input[i] == '.')
          {
               isExtensionFound = true;
               break;
          }
     }

     if (!isExtensionFound)
     {
          string fileExtension;

          cout << "Please specify a file extension: ";
          cin >> fileExtension;
          cin.ignore();

          for (int i = 0; i < fileExtension.length(); i++)
          {
               if (fileExtension[i] == '.')
               {
                    input += fileExtension;
                    break;
               }
               else
               {
                    input += "." + fileExtension;
                    break;
               }
          }
     }

     return input;
}

void generateBinaryFile(int n)
{
}

int main()
{
     cout << endl
          << "/////////////////////////////////////////////////////////////" << endl
          << endl;

     char userDecision;
     string fileName;

     cout << "Do you have a file to read from? (Y | N) ";
     cin >> userDecision;

     if (userDecision == 'N' || userDecision == 'n')
     {
          cout << "Would you like to create a binary file with random numbers? (Y | N) ";
          cin >> userDecision;
          if (userDecision == 'N' || userDecision == 'n')
               return 0;
          else
          {
               int numberOfElements = 0;
               cout << "How many elements to generate? ";
               cin >> numberOfElements;

               generateBinaryFile(numberOfElements);
          }
     }
     else
          fileName = fileNameInput();

     cout << endl
          << "/////////////////////////////////////////////////////////////" << endl
          << endl;
     return 0;
}