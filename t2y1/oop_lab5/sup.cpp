#include <bits/stdc++.h>
#include "sup.h"
#include "../../lib.h"
using namespace std;

/*
Варіант 5. Створити динамічний клас для роботи з рядками (послідовностями символів). Максимальна довжина послідовності – 65535, код завершення послідовності – нуль. Здійснити перевантаження символів операцій:
"="	– динамічне присвоєння,
" << " , " >> " – консольне введення-виведення значень;
" << " , " >> "  - введення із файлу і виведення у файл з символами таким чином:
f << A або A >> f – виведення (запис) значення A в файл f,
f >> A або A << f – введення (читання) значення A з файлу f.
*/

class DynamicString
{
private:
    char *strValue; // pointer to the string value
    size_t strSize; // size of the string value

public:
    // declare default constructor
    DynamicString() : strValue(nullptr), strSize(0) {}

    // define a parameterized constructor
    DynamicString(const char *INPUT) : strValue(nullptr), strSize(0)
    {
        // check if the value of INPUT is not null
        if (INPUT)
        {
            // if it's not null, determine the length of the INPUT string and add 1 to it, taking the null terminator into account
            strSize = strlen(INPUT) + 1;
            // allocate an array of strSize characters and assign it to strValue
            strValue = new char[strSize];
            // copy the contents of the INPUT string to strValue
            strcpy_s(strValue, strSize, INPUT);
        }
    }

    // declare method for overloading the assignment operator
    DynamicString &operator=(const char *INPUT)
    {
        // check if input is valid and not empty
        if (INPUT)
        {
            // calculate the size of the string
            size_t inputSize = strlen(INPUT) + 1;

            // create a new character array to hold the input string
            char *tempStringHolder = new char[inputSize];
            // copy the contents of the input string to the new character array
            strcpy_s(tempStringHolder, inputSize, INPUT);

            // free the memory for the previously stored value
            delete[] strValue;
            // set the DynamicString object's strValue to the new character array holding the input string
            strValue = tempStringHolder;
            // update the size to the size of the input string
            strSize = inputSize;
        }
        // return the DynamicString object by reference
        return *this;
    }

    // create friend functions for console output
    friend ostream &operator<<(ostream &outputStream, const DynamicString &OUTPUT); // console output operator
    friend istream &operator>>(istream &inputStream, DynamicString &inputHolder);   // console input operator

    // create friend functions for file output
    friend ofstream &operator<<(ofstream &outputStream, const DynamicString &OUTPUT); // file output operator
    friend ifstream &operator>>(ifstream &inputStream, DynamicString &inputHolder);   // file input operator

    // declare destructor
    ~DynamicString()
    {
        // delete the string
        delete[] strValue;
    }
};

// define an output stream operator function
ostream &operator<<(ostream &outputStream, const DynamicString &OUTPUT)
{
    // output the string value of the DynamicString object to the output stream
    outputStream << OUTPUT.strValue;
    // return the output stream
    return outputStream;
}

// define an input stream operator function
istream &operator>>(istream &inputStream, DynamicString &inputHolder)
{
    // define a character array to store input
    char buffer[65536];
    // use the getline function to read input from an input stream and store it in the buffer array
    inputStream.getline(buffer, 65536);
    // convert the buffer array to a DynamicString object and store it in inputHolder
    inputHolder = buffer;
    // return the input stream
    return inputStream;
}

// define an output stream operator function for file
ofstream &operator<<(ofstream &outputStream, const DynamicString &OUTPUT)
{
    // write the value of strValue to output
    outputStream << OUTPUT.strValue;
    // return the output stream
    return outputStream;
}

// define an input stream operator function for file
ifstream &operator>>(ifstream &inputStream, DynamicString &inputHolder)
{
    // define a character array to store input
    char buffer[65536];
    // use the getline function to read input from an input stream and store it in the buffer array
    inputStream.getline(buffer, 65536);
    // convert the buffer array to a DynamicString object and store it in inputHolder
    inputHolder = buffer;
    // return the input stream
    return inputStream;
}

// define a function for outputting the array of strings
void showStrings(vector<DynamicString> &container)
{
    // get the size of container
    ll containerSize = container.size();
    // check if container is empty
    if (containerSize == 0)
    {
        // if so, output error and stop function execution
        bad("No strings to display");
        return;
    }

    // loop through each element and print it
    for (ll i = 0; i < containerSize; i++)
        cout << "- " << container[i] << endl;
    return;
}

void showStrings(vector<DynamicString> &container, const string &OUTPUT_FILENAME)
{
    // get the size of container
    ll containerSize = container.size();
    // check if container is empty
    if (containerSize == 0)
    {
        // if so, output error and stop function execution
        bad("No strings to output");
        return;
    }

    ofstream outputFile(OUTPUT_FILENAME);
    if (!outputFile.is_open())
    {
        bad("Couldn't open output file");
        return;
    }

    outputFile << "==============================\n\n";
    for (ll i = 0; i < containerSize; i++)
        outputFile << container[i] << endl;
    outputFile << "==============================\n\n";

    outputFile.close();
    good("Strings successfully outputted");
    return;
}

// define a function for outputting the array of strings
void addStrings(vector<DynamicString> &container)
{
    cout << "Enter the number of strings to add: ";
    ll stringCount = getNum();
    // check if container is empty
    if (stringCount < 1)
    {
        // if so, output error and stop function execution
        bad("Enter a positive amount of strings to add");
        return;
    }

    // loop through each element and print it
    for (ll i = 0; i < stringCount; i++)
    {
        DynamicString stringHolder;
        cout << "- ";
        cin >> stringHolder;
        container.eb(stringHolder);
        cout << endl;
    }
    return;
}

void addStrings(vector<DynamicString> &container, const string &INPUT_FILENAME)
{
    // declare file instance
    ifstream inputFile(INPUT_FILENAME);
    // check if file cannot be opened
    if (!inputFile.is_open())
    {
        // if so output the error and stop function execution
        bad("Input file cannot be opened");
        return;
    }

    // declare variables for proecessing the lines of file
    vector<string> linesFromFile;
    string lineHolder;
    ll linesCounter = 1;

    // get all file lines
    while (getline(inputFile, lineHolder))
    {
        // check if a line is empty which will indicate the new item
        if (lineHolder.empty())
            // if it is increment the counter
            linesCounter++;
        // if its not
        else
            // add line to vector
            linesFromFile.pb(lineHolder);
    }

    // create specified amount of objects using a for loop
    for (ll i = 0; i < linesCounter; i++)
    {
        DynamicString stringHolder = linesFromFile[i].c_str();
        container.eb(stringHolder);
    }

    // end function execution
    good("Strings successfully added");
    return;
}

// for showing the main menu of the application
void outputMenu(vector<DynamicString> &container)
{
    // output the menu
    cout << BOLD << "Welcome! Choose some option from below\n"
         << UNBOLD;
    cout << "1. Show strings\n";
    cout << "2. Add strings\n";
    cout << "3. Remove strings\n";
    cout << "4. Exit\n";
    // ask user to enter their choice
    cout << "Enter: ";
    // and validate it
    ll userDecision = getNum();
    cout << endl;

    // if user chose to just show route
    if (userDecision == 1)
    {
        cout << BOLD << "Where to output the string?\n"
             << UNBOLD;
        cout << "1. To console\n";
        cout << "2. To file\n";
        cout << "3. Exit\n";
        userDecision = getNum();
        cout << endl;

        if (userDecision == 1)
        {
            showStrings(container);
        }
        else if (userDecision == 2)
        {
            string outputFileName = "D:/repos/university/t2y1/oop_lab5/";
            outputFileName += getFileName();
            showStrings(container, outputFileName.c_str());
        }
    }
    // if user chose to just show route
    else if (userDecision == 2)
    {
        cout << BOLD << "Where to get strings from?\n"
             << UNBOLD;
        cout << "1. From console\n";
        cout << "2. From file\n";
        cout << "3. Exit\n";
        userDecision = getNum();
        cout << endl;

        if (userDecision == 1)
        {
            addStrings(container);
        }
        else if (userDecision == 2)
        {
            string inputFileName = "D:/repos/university/t2y1/oop_lab5/";
            inputFileName += getFileName();
            addStrings(container, inputFileName.c_str());
        }
    }
    // if user chose to just show route
    else if (userDecision == 3)
    {
    }
}