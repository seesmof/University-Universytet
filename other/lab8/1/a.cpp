// include necessary libraries
#include <bits/stdc++.h>
using namespace std;

// function prototypes //
void outputEnding();
bool isReadable(const string &);
int countLines(const string &);
string randString(int);
void generateBinaryFile(int, const string &);
string fileNameInput();
void resultCalc(int n, const string &input, const string &output);

/////////////////////////

// declare main function
int main()
{
    // declare local variables //
    srand(time(NULL));
    char doContinue;
    string inputFileName, outputFileName;
    int numOfLines;
    int randomNumOfLetters = rand() % 10;
    /////////////////////////////

    // project intro
    cout << endl
         << "/////////////////////////////////////////////////////////////" << endl
         << endl
         << "Welcome! This is a program for Part 2 | 4.3.2.1" << endl
         << endl
         << "/////////////////////////////////////////////////////////////" << endl
         << endl;
    do
    {
        //////////////////////////////////////////////////////////////////////////////////
        char userDecision;
        cout << "Do you have a file to read from? (Y | N): ";
        cin >> userDecision;

        if (userDecision == 'N' || userDecision == 'n')
        {
            cout << endl;
            cout << "Would you like to generate one? (Y | N): ";
            cin >> userDecision;

            if (userDecision == 'N' || userDecision == 'n')
            {
                outputEnding();
                break;
            }

            cout << "Enter number of lines to generate: ";
            cin >> numOfLines;

            inputFileName = randString(randomNumOfLetters);
            generateBinaryFile(numOfLines, inputFileName);
        }
        else
        {
            cout << endl;
            inputFileName = fileNameInput();
            numOfLines = countLines(inputFileName);
        }

        outputFileName = randString(randomNumOfLetters);
        resultCalc(numOfLines, inputFileName, outputFileName);

        //////////////////////////////////////////////////////////////////////////////////
        cout << endl
             << endl
             << "/////////////////////////////////////////////////////////////" << endl
             << endl
             << "Would you like to continue program execution? (Y | N): ";
        cin >> doContinue;
        if (doContinue == 'N' || doContinue == 'n')
        {
            outputEnding();
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

void resultCalc(int n, const string &input, const string &output)
{
    int absResult;
    int secondLine, secondToLastLine;
    fstream iFile(input, ios::binary);
    fstream oFile(output, ios::binary);

    int lineCounter = 1;
    string lineHolder;
    for (int i = 0; i < n; i++)
    {
        if (n < 4)
        {
            cout << "ERROR: Number of lines is insufficient for successful calculation." << endl;
            return;
        }

        while (getline(iFile, lineHolder))
        {
            cout << lineHolder << endl;
            lineCounter++;
            cout << lineCounter << " count" << endl
                 << endl;
        }
    }
}

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

// create a function that will generate the binary file with random numbers
void generateBinaryFile(int n, const string &fileName)
{
    // declare local variables
    cout << endl;
    fstream file(fileName.c_str(), ios::binary);
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
        // fill buffer with random number
        int randTemp = rand() % 100;
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

    // add file extension to result
    result += ".bin";
    // return result
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
bool isReadable(const string &fileName)
{
    // declare local variables for reading a file
    fstream file(fileName, ios::in | ios::out);

    // if result file is successfully opened
    if (file.good())
    {
        // output successs message
        cout << fileName << " is working properly.";
        return true;
    }
    else
    {
        // if not, output failure message
        cout << "ERROR: Could not open file " << fileName;
        return false;
    }
}

void outputEnding()
{
    cout << endl
         << "Thanks for using this program." << endl
         << endl
         << "/////////////////////////////////////////////////////////////" << endl
         << endl;
    return;
}