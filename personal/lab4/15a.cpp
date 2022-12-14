// include necessary libraries
#include <iostream>
#include <string.h>
using namespace std;

// declare main function
int main(int argc, char **argv)
{
    // output program intro
    cout << endl;
    cout << "****************************** Test A *************************************" << endl
         << endl;

    // declare input string
    char input[1024];

    // ask user to enter input string
    cout << "Enter the string: ";
    cin.getline(input, sizeof(input));

    // create wanted letter variable and ask user to enter it
    char letter;
    cout << "Enter a wanted letter: ";
    cin >> letter;

    // create a function that will look for words in the input string that start with this letter
    int wantedWordCount = 0; // declare counter variable
    for (int i = 0, size = strlen(input); i < size; i++)
    {
        // for first words in a sentence look for letter right away
        if (i == 0)
        {
            if (input[i] == letter)
            {
                // if found => counter++
                wantedWordCount++;
            }
        }
        // for any words that are not first look for a space and a wanted letter after it
        else
        {
            if (input[i] == ' ' && input[i + 1] == letter)
            {
                // if found => counter++
                wantedWordCount++;
            }
        }
    }

    // output the result
    cout << endl;
    cout << "In the following text there is " << wantedWordCount << " words that begin with " << letter << endl;

    // output project outro
    cout << endl;
    cout << "***************************************************************************" << endl
         << endl;

    // end main function
    return 0;
}