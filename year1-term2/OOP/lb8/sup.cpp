#include "sup.h"
#include "D:\repos\university\lib.h"

const string ROOT_DIR = "D:/repos/university/year1-term2/OOP/lb8/";

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

void showStrings(vector<DynamicString> &container, const string &FILE)
{
    ll stringsNum = container.size();
    if (stringsNum == 0)
    {
        bad("No strings found");
        return;
    }

    ofstream file(FILE);
    if (!file.is_open())
    {
        bad("File could not be opened");
        return;
    }

    file << "==============================\n\n";
    file << "Available strings (" << stringsNum << "):\n";
    for (ll i = 0; i < stringsNum; i++)
    {
        file << i + 1 << ". " << container[i] << endl;
    }
    file << "\n==============================\n\n";
    file.close();

    if (file.good())
        good("Strings succesfully saved");
    else
        bad("Strings were not saved");
}

void addStrings(vector<DynamicString> &container)
{
    ll initSize = container.size();

    cout << "Enter number of strings to add: ";
    ll numToAdd = getNum();
    cout << endl;
    cin.ignore();

    if (numToAdd < 1)
    {
        bad("Enter a valid number of strings");
        return;
    }

    for (ll i = 0; i < numToAdd; i++)
    {
        DynamicString value;
        cout << i + 1 << ". Enter value: ";
        cin >> value;
        container.eb(value);
    }
    cout << endl;

    if (container.size() == initSize + numToAdd)
        good("Strings succesfully added");
    else
        bad("Strings were not added");

    cout << endl;
    showStrings(container);
}

void addStrings(vector<DynamicString> &container, const string &FILE)
{
    ll initSize = container.size();
    ifstream file(FILE);
    string line;
    vector<string> lines;

    if (!file.is_open())
    {
        bad("File not found");
        return;
    }

    while (getline(file, line))
    {
        lines.push_back(line);
    }
    file.close();

    for (ll i = 0; i < lines.size(); i++)
    {
        DynamicString stringHolder = lines[i].c_str();
        container.eb(stringHolder);
    }

    if (container.size() == initSize + lines.size())
        good("Strings succesfully added");
    else
        bad("Strings were not added");
}

void removeString(vector<DynamicString> &container)
{
    ll initSize = container.size();

    if (initSize == 0)
    {
        bad("No strings found");
        return;
    }

    cout << endl;
    showStrings(container);
    cout << endl;

    cout << "Enter number of string to remove: ";
    ll numToRemove = getNum();
    numToRemove--;

    if (numToRemove < 0 || numToRemove >= initSize)
    {
        bad("Enter a valid number string number");
        return;
    }

    container.erase(container.begin() + numToRemove);
    cout << endl;

    if (container.size() == initSize - 1)
        good("String succesfully removed");
    else
        bad("String was not removed");
}

void outputMenu(vector<DynamicString> &container)
{
    vector<string> menuItems = {
        "Show strings",
        "Add strings",
        "Remove strings",
        "Exit"};
    ll userDecision = showMenu(menuItems);

    if (userDecision == 1)
    {
        menuItems = {
            "Output to console",
            "Output to file",
            "Exit"};
        userDecision = showMenu(menuItems);

        if (userDecision == 1)
        {
            showStrings(container);
        }
        else if (userDecision == 2)
        {
            string fileName = ROOT_DIR;
            fileName += getFileName();
            showStrings(container, fileName);
        }
    }
    else if (userDecision == 2)
    {
        menuItems = {
            "Add strings from console",
            "Add strings from file",
            "Exit"};
        userDecision = showMenu(menuItems);

        if (userDecision == 1)
        {
            addStrings(container);
        }
        else if (userDecision == 2)
        {
            string fileName = ROOT_DIR;
            fileName += getFileName();
            addStrings(container, fileName);
        }
    }
    else if (userDecision == 3)
    {
        removeString(container);
    }
}