#include "sup.h"
#include "D:\repos\university\lib.h"

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

void showStrings(vector<DynamicString> &container)
{
    ll containerSize = container.size();
    if (containerSize == 0)
    {
        bad("No strings to display");
        return;
    }

    cout << "Available strings (" << containerSize << "):\n";
    for (ll i = 0; i < containerSize; i++)
    {
        cout << i + 1 << ". " << container[i] << endl;
    }
    return;
}

void showStrings(vector<DynamicString> &container, const string &OUTPUT_FILENAME)
{
    ll containerSize = container.size();
    if (containerSize == 0)
    {
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
    {
        outputFile << i + 1 << ". ";
        outputFile << container[i] << endl;
    }
    outputFile << "\n==============================\n\n";

    outputFile.close();
    cout << endl;
    good("Strings successfully outputted");
    return;
}

void addStrings(vector<DynamicString> &container)
{
    cout << "Enter the number of strings to add: ";
    ll stringCount = getNum();
    cin.ignore();
    if (stringCount < 1)
    {
        bad("Enter a positive amount of strings to add");
        return;
    }

    cout << "Add strings below (" << stringCount << "): \n";
    for (ll i = 0; i < stringCount; i++)
    {
        DynamicString stringHolder;
        cout << i + 1 << ". ";
        cin >> stringHolder;
        container.eb(stringHolder);
        cout << endl;
    }
    return;
}

void addStrings(vector<DynamicString> &container, const string &INPUT_FILENAME)
{
    ifstream inputFile(INPUT_FILENAME);
    if (!inputFile.is_open())
    {
        bad("Input file cannot be opened");
        return;
    }

    vector<string> linesFromFile;
    string lineHolder;
    ll linesCounter = 0;

    while (getline(inputFile, lineHolder))
    {
        linesCounter++;
        linesFromFile.pb(lineHolder);
    }

    for (ll i = 0; i < linesCounter; i++)
    {
        DynamicString stringHolder = linesFromFile[i].c_str();
        container.eb(stringHolder);
    }

    cout << endl;
    good("Strings successfully added");
    return;
}

void removeString(vector<DynamicString> &container)
{
    if (container.size() == 0)
    {
        bad("No strings to remove");
        return;
    }
    else
    {
        cout << "Enter index of element to delete: ";
        ll index = getNum();
        index--;
        if (index < 0 || index >= container.size())
        {
            bad("Index out of range");
            return;
        }
        cout << endl;
        good("Element successfully removed");
        cout << endl;
        container.erase(container.begin() + index);
        return;
    }
}

void outputMenu(vector<DynamicString> &container)
{
    cout << BOLD << "Welcome! Choose some option from below\n"
         << UNBOLD;
    cout << "1. Show strings\n";
    cout << "2. Add strings\n";
    cout << "3. Remove strings\n";
    cout << "4. Exit\n";
    cout << "Enter: ";
    ll userDecision = getNum();
    cout << endl;

    if (userDecision == 1)
    {
        cout << BOLD << "Where to output the string?\n"
             << UNBOLD;
        cout << "1. To console\n";
        cout << "2. To file\n";
        cout << "3. Exit\n";
        cout << "Enter: ";
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
    else if (userDecision == 2)
    {
        cout << BOLD << "Where to get strings from?\n"
             << UNBOLD;
        cout << "1. From console\n";
        cout << "2. From file\n";
        cout << "3. Exit\n";
        cout << "Enter: ";
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
    else if (userDecision == 3)
    {
        showStrings(container);

        removeString(container);

        showStrings(container);
    }
}