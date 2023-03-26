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

// string inputFileName = "D:/repos/university/t2y1/tasks/oop_lab4/";

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
        }
        else if (userDecision == 2)
        {
            string inputFileName = "D:/repos/university/t2y1/tasks/oop_lab5/";
            inputFileName += getFileName();
        }
    }
    // if user chose to just show route
    else if (userDecision == 2)
    {
    }
    // if user chose to just show route
    else if (userDecision == 3)
    {
    }
}