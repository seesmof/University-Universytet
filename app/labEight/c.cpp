// include necessary libraries
#include <bits/stdc++.h>
using namespace std;

// create a function that will take file name from user
string fileNameInput()
{
    // declare local variables
    bool isExtensionFound = false;
    string input;

    // ask user to input file name
    cout << "Enter the name of the file: ";
    cin >> input;
    cin.ignore();

    // create for loop to look for extension
    for (int i = 0; i < input.length(); i++)
    {
        // dot is an indication of extension
        if (input[i] == '.')
        {
            // if found then change bool isExtensionFound to true
            isExtensionFound = true;
            break; // break out of loop
        }
    }

    // if the result is not found then
    if (!isExtensionFound)
    {
        // create a new string for holding the file extension
        string fileExtension;

        // ask user to enter a file extension
        cout << "Please specify a file extension: ";
        cin >> fileExtension;
        cin.ignore();

        // create a for loop
        for (int i = 0; i < fileExtension.length(); i++)
        {
            // look for a dot in input
            if (fileExtension[i] == '.')
            {
                // if found then add it to the result string
                input += fileExtension;
                break; // break out of loop
            }
            else
            {
                // if not found then add add a dot + input to the result string
                input += "." + fileExtension;
                break; // break out of loop
            }
        }
    }

    // return the result string
    return input;
}

// create a function that will generate file with random numbers
void generateRandFile(int n, const string &fileName)
{
    // declare local variables
    cout << endl;
    fstream file(fileName.c_str());
    // open the file to work with it
    file.open(fileName.c_str(), ios::out);

    // if file is not open
    if (!file.is_open())
    {
        // output error message
        cout << "ERROR: Couldn't open " << fileName << endl;
        return; // end function
    }

    // create a for loop
    for (int i = 0; i < n; i++)
    {
        int randTemp;
        do
        {
            int randTemp = rand() % 10 - 10;

        } while (randTemp != 0);
        cout << randTemp << endl;
        // output that buffer to file
        file << randTemp << endl;
    }

    // close the file
    file.close();
    // end function
    return;
}

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
    result += ".txt";
    return result;
}

// declare function that will count lines in file
int countLines(const string &a)
{
    // declare local variables
    int count = 0;
    string line;
    ifstream aFile(a.c_str(), ios::in | ios::binary);

    // while we can get a line from the file
    while (getline(aFile, line))
        // increment count
        count++;
    // return number of lines
    return count; // end function
}

// declare function to check whether a file is readable
void isReadable(const string &fileName)
{
    // declare local variables for reading a file
    fstream file(fileName, ios::in | ios::out);

    // if result file is successfully opened
    if (file.good())
        // output successs message
        cout << fileName << " is working properly.";
    else
        // if not, output failure message
        cout << "ERROR: Could not open file " << fileName;
}

void result()
{
    // variables

    // two vectors - one for negative and one for positive

    // for loop through lines

    // if found < 0, pushback to negative, else pushback to positive

    // output all to result file
}

// declare main function
int main()
{
    // declare local variables
    srand(time(NULL));
    char userDecision;
    string inFileName, outFileName;
    int numOfLets = rand() % (10 - 2 + 1) + 2;

    // project intro
    cout << endl
         << "/////////////////////////////////////////////////////////////" << endl
         << endl
         << "Welcome! This program will manipulate binary files." << endl
         << endl
         << "/////////////////////////////////////////////////////////////" << endl
         << endl;
    char doContinue;
    do
    {
        //////////////////////////////////////////////////////////////////////////////////
        cout << "Do you have a file to read from? (Y | N): ";
        cin >> userDecision;
        cin.ignore();

        if (userDecision == 'N' || userDecision == 'n')
        {
            cout << "Would you like to generate one? (Y | N): ";
            cin >> userDecision;
            cin.ignore();

            if (userDecision == 'N' || userDecision == 'n')
            {
                cout << endl
                     << "Thanks for using this program." << endl
                     << endl
                     << "/////////////////////////////////////////////////////////////" << endl
                     << endl;
                break;
            }

            cout << "How many letters do you want your file name to be?: ";
            cin >> numOfLets;
            int numOfNums;
            cout << "How many numbers to generate? (min 4): ";
            cin >> numOfNums;

            inFileName = randString(numOfLets);
            generateRandFile(numOfNums, inFileName);
            isReadable(inFileName);
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
    return 0;
}