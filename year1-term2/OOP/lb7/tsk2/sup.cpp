#include "sup.h"
#include "D:\repos\university\lib.h"

// Виконати завдання з лабораторної роботи #5 з довільним типом даних

class DynamicString
{
private:
public:
};

void showStrings(vector<DynamicString> &container)
{
}

void addStrings(vector<DynamicString> &container)
{
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