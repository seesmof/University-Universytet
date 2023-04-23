#include "sup.h"
#include "D:\repos\university\lib.h"

// Для завдання з лабораторної роботи #5 виконати обробку виняткових ситуацій з використанням класу Exception.

class DynamicString
{
private:
    char *strValue;
    size_t strSize;

public:
    DynamicString() : strValue(nullptr), strSize(0) {}
    DynamicString(const char *INPUT) : strValue(nullptr), strSize(0)
    {
        if (INPUT)
        {
            strSize = strlen(INPUT) + 1;
            strValue = new char[strSize];
            strcpy_s(strValue, strSize, INPUT);
        }
    }
    DynamicString(const DynamicString &other)
    {
        size_t len = strlen(other.strValue) + 1;
        strValue = new char[len];
        strcpy_s(strValue, len, other.strValue);
    }
    DynamicString &operator=(const char *INPUT)
    {
        delete[] strValue;
        size_t inputSize = strlen(INPUT) + 1;
        strValue = new char[inputSize];
        strcpy_s(strValue, inputSize, INPUT);
        return *this;
    }
    DynamicString &operator=(const DynamicString &INPUT)
    {
        delete[] strValue;
        strSize = INPUT.strSize;
        strValue = new char[strSize + 1];
        strcpy(strValue, INPUT.strValue);
        return *this;
    }
    friend ostream &operator<<(ostream &outputStream, const DynamicString &OUTPUT)
    {
        outputStream << OUTPUT.strValue;
        return outputStream;
    }
    friend istream &operator>>(istream &inputStream, DynamicString &inputHolder)
    {
        char buffer[65536];
        inputStream.getline(buffer, 65536);
        inputHolder = buffer;
        return inputStream;
    }
    friend ofstream &operator<<(ofstream &outputStream, const DynamicString &OUTPUT)
    {
        outputStream << OUTPUT.strValue;
        return outputStream;
    }
    friend ifstream &operator>>(ifstream &inputStream, DynamicString &inputHolder)
    {
        char buffer[65536];
        inputStream.getline(buffer, 65536);
        inputHolder = buffer;
        return inputStream;
    }
    ~DynamicString()
    {
        delete[] strValue;
    }
};

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
    cout << "Available strings (" << containerSize << "):\n";
    for (ll i = 0; i < containerSize; i++)
    {
        cout << i + 1 << ". " << container[i] << endl;
    }
    return;
}

// define a function for outputting the container of strings to the file
void showStrings(vector<DynamicString> &container, const string &OUTPUT_FILENAME)
{
    // set containerSize to the size of the container
    ll containerSize = container.size();
    // if container is empty
    if (containerSize == 0)
    {
        // print error message and end function execution
        bad("No strings to output");
        return;
    }

    // create a new output file with the name specified in argument
    ofstream outputFile(OUTPUT_FILENAME);
    // if the file couldn't be opened
    if (!outputFile.is_open())
    {
        // print an error message and stop function execution
        bad("Couldn't open output file");
        return;
    }

    // output a separator line before the start of the strings
    outputFile << "==============================\n\n";
    // loop through each element of the container and output it to the outputFile
    for (ll i = 0; i < containerSize; i++)
    {
        outputFile << i + 1 << ". ";
        outputFile << container[i] << endl;
    }
    // output a separator line after the end of the strings
    outputFile << "\n==============================\n\n";

    // close the outputFile
    outputFile.close();
    // indicate successful output
    cout << endl;
    good("Strings successfully outputted");
    // return
    return;
}

// define a function for outputting the array of strings
void addStrings(vector<DynamicString> &container)
{
    // ask the user for the number of strings to add
    cout << "Enter the number of strings to add: ";
    ll stringCount = getNum();
    // ignore any input entered before getting the number of strings
    cin.ignore();
    // if the number of strings is less than 1
    if (stringCount < 1)
    {
        // display the error message and exit the program
        bad("Enter a positive amount of strings to add");
        return;
    }

    // prompt the user to enter the specified number of strings
    cout << "Add strings below (" << stringCount << "): \n";
    // for each string to add
    for (ll i = 0; i < stringCount; i++)
    {
        // create a DynamicString to hold the new string
        DynamicString stringHolder;
        // prompt the user to enter the new string
        cout << i + 1 << ". ";
        cin >> stringHolder;
        // add the DynamicString to the container
        container.eb(stringHolder);
        cout << endl;
    }
    // axit the function
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
    ll linesCounter = 0;

    // get all file lines
    while (getline(inputFile, lineHolder))
    {
        // increment the counter
        linesCounter++;
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
    cout << endl;
    good("Strings successfully added");
    return;
}

// define a function for removing an object from the container
void removeString(vector<DynamicString> &container)
{
    // check if the container is empty
    if (container.size() == 0)
    {
        // output error message and exit program
        bad("No strings to remove");
        return;
    }
    else
    {
        // ask the user for the index of the element they want to remove
        cout << "Enter index of element to delete: ";
        ll index = getNum();
        index--;
        // if the user entered an invalid index
        if (index < 0 || index >= container.size())
        {
            // print error message and exit program
            bad("Index out of range");
            return;
        }
        // if the index is valid print a success message
        cout << endl;
        good("Element successfully removed");
        cout << endl;
        // remove the element at the specified index from the vector
        container.erase(container.begin() + index);
        // exit the function
        return;
    }
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

    // if user chose to show the strings
    if (userDecision == 1)
    {
        // print a message asking where to output the string
        cout << BOLD << "Where to output the string?\n"
             << UNBOLD;
        // print options to console
        cout << "1. To console\n";
        cout << "2. To file\n";
        cout << "3. Exit\n";
        cout << "Enter: ";
        // get the user's input
        userDecision = getNum();
        cout << endl;

        // if the user chose to output to console
        if (userDecision == 1)
        {
            // display the string container to the console
            showStrings(container);
        }
        // else, if the user chose to output to file
        else if (userDecision == 2)
        {
            // create a file path to hold the output file name
            string outputFileName = "D:/repos/university/t2y1/oop_lab5/";
            // append the user's selected filename to the output file name
            outputFileName += getFileName();
            // display the string container to a file with the specified file name
            showStrings(container, outputFileName.c_str());
        }
    }
    // if user chose to add new strings
    else if (userDecision == 2)
    {
        // output a message asking where to get strings from
        cout << BOLD << "Where to get strings from?\n"
             << UNBOLD;
        // output options for getting strings
        cout << "1. From console\n";
        cout << "2. From file\n";
        cout << "3. Exit\n";
        // ask the user to enter their choice
        cout << "Enter: ";
        // get the user's choice as a number
        userDecision = getNum();
        cout << endl;

        // if the user chose to get strings from the console
        if (userDecision == 1)
        {
            // call the function to add strings to the container from the console
            addStrings(container);
        }
        // if the user chose to get strings from a file
        else if (userDecision == 2)
        {
            // set the path of the input file to a default path and the name entered by the user
            string inputFileName = "D:/repos/university/t2y1/oop_lab5/";
            inputFileName += getFileName();

            // call the function to add strings to the container from the file with the given path
            addStrings(container, inputFileName.c_str());
        }
    }
    // if user chose to remove strings from the container
    else if (userDecision == 3)
    {
        // display the strings in the container
        showStrings(container);

        // remove a string from the container
        removeString(container);

        // display the updated container with the removed string
        showStrings(container);
    }
}