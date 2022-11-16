// include necessary libraries
#include <iostream>
using namespace std;

// This function receives text and shift and
// returns the encrypted text
string encrypt(string text, int s)
{
     string result = "";

     // traverse text
     for (int i = 0; i < text.length(); i++)
     {
          // apply transformation to each character
          // Encrypt Uppercase letters
          if (isupper(text[i]))
               result += char(int(text[i] + s - 65) % 26 + 65);

          // Encrypt Lowercase letters
          else
               result += char(int(text[i] + s - 97) % 26 + 97);
     }

     // Return the resulting string
     return result;
}
// declare main function
int main(int argc, char **argv)
{
     // output program intro
     cout << endl;
     cout << "****************************** Test Task *************************************" << endl
          << endl;

     string text;
     cout << "Enter text: ";
     getline(cin, text);

     int s;
     cout << "Enter a key: ";
     cin >> s;

     cout << "Text : " << text;
     cout << "\nShift: " << s;
     cout << "\nCipher: " << encrypt(text, s);

     // output project outro
     cout << endl;
     cout << "******************************************************************************" << endl
          << endl;

     // end main function
     return 0;
}