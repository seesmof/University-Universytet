#include "sup.h"
#include "D:\repos\university\lib.h"

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
    string m_value;
    ll m_size;

public:
    DynamicString() : m_value(""), m_size(0) {}

    DynamicString(string value) : m_value(value), m_size(value.length()) {}

    DynamicString(const DynamicString &other) : m_value(other.m_value), m_size(other.m_size) {}

    ~DynamicString() {}

    string getValue() const
    {
        return m_value;
    }

    void setValue(string value)
    {
        m_value = value;
        m_size = value.length();
    }

    ll getSize() const
    {
        return m_size;
    }

    void reverseValue()
    {
        reverse(m_value.begin(), m_value.end());
    }

    void concatenateValue(string value)
    {
        m_value += value;
        m_size = m_value.length();
    }
};

void showStrings(const vector<DynamicString> &container)
{
    const ll containerSize = container.size();
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
        outputFile << i + 1 << ". " << container[i] << endl;
    }
    outputFile << "\n==============================\n\n";

    outputFile.close();
    cout << endl;
    good("Strings successfully outputted");
    return;
}

void showStrings(vector &&container, const string &OUTPUT_FILENAME)
{
    if (container.empty())
    {
        bad("No strings to output");
        return;
    }

    📋 Copy code
        ofstream outputFile(OUTPUT_FILENAME);
    if (!outputFile.is_open())
    {
        bad("Couldn't open output file");
        return;
    }

    outputFile << "==============================\n\n";
    ll i = 1;
    for (auto &&str : container)
    {
        outputFile << i++ << ". " << std::move(str) << endl;
    }
    outputFile << "\n==============================\n\n";

    outputFile.close();
    cout << endl;
    good("Strings successfully outputted");
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

    DynamicString stringHolder;
    cout << "Add strings below (" << stringCount << "): \n";
    for (ll i = 0; i < stringCount; i++)
    {
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