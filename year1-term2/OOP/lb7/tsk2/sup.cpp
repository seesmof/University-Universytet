#include "sup.h"
#include "D:\repos\university\lib.h"

// Виконати завдання з лабораторної роботи #5 з довільним типом даних

class DynamicString
{
private:
    string m_value;
    ll m_size;

public:
    DynamicString() : m_value(""), m_size(0) {}
    DynamicString(string value) : m_value(value), m_size(value.length()) {}
    void setValue(string value)
    {
        m_value = value;
        m_size = value.length();
    }
    string getValue() const { return m_value; }
    ll getSize() const { return m_size; }
    void m_reverse() { reverse(m_value.begin(), m_value.end()); }
    void m_replace(string replaceThis, string withThis) { m_value.replace(m_value.find(replaceThis), replaceThis.length(), withThis); }
    void m_remove_spaces() { m_value.erase(remove(m_value.begin(), m_value.end(), ' '), m_value.end()); }
    void m_to_upper() { transform(m_value.begin(), m_value.end(), m_value.begin(), ::toupper); }
    void m_to_lower() { transform(m_value.begin(), m_value.end(), m_value.begin(), ::tolower); }
    void m_find_substring(string substring) { m_value.find(substring); }
    ~DynamicString() {}
};

void showStrings(vector<unique_ptr<DynamicString>> &container)
{
    ll stringsNum = container.size();
    if (stringsNum == 0)
    {
        bad("No strings found");
        return;
    }

    cout << "Available strings (" << stringsNum << "):\n";
    for (ll i = 0; i < stringsNum; i++)
    {
        cout << i + 1 << ". " << container[i]->getValue() << " - " << container[i]->getSize() << " symbols\n";
    }
}

void showStrings(vector<unique_ptr<DynamicString>> &container, const string &FILE)
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

    for (ll i = 0; i < stringsNum; i++)
    {
        file << i + 1 << ". " << container[i]->getValue() << " - " << container[i]->getSize() << " symbols\n";
    }
    file.close();
}

void addStrings(vector<unique_ptr<DynamicString>> &container)
{
    ll initSize = container.size();

    cout << "Enter number of strings to add: ";
    ll numToAdd = getNum();
    cout << endl;
    cin.ignore();

    if (numToAdd == 0)
    {
        bad("Enter a valid number of strings");
        return;
    }

    for (ll i = 0; i < numToAdd; i++)
    {
        string value;
        cout << i + 1 << ". Enter value: ";
        getline(cin, value);
        container.push_back(make_unique<DynamicString>(value));
    }
    cout << endl;

    if (container.size() == initSize + numToAdd)
        good("Strings succesfully added");
    else
        bad("Strings were not added");

    cout << endl;
    showStrings(container);
}

void addStrings(vector<unique_ptr<DynamicString>> &container, const string &FILE)
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

    for (auto &line : lines)
    {
        container.push_back(make_unique<DynamicString>(line));
    }

    if (container.size() == initSize + lines.size())
        good("Strings succesfully added");
    else
        bad("Strings were not added");
}

void removeString(vector<unique_ptr<DynamicString>> &container)
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

    cout << endl;
    showStrings(container);
}

void modifyString(vector<unique_ptr<DynamicString>> &container)
{
    if (container.size() == 0)
    {
        bad("No strings found");
        return;
    }

    cout << endl;
    showStrings(container);
    cout << endl;

    cout << "Enter number of string to modify: ";
    ll numToModify = getNum();
    numToModify--;
    cout << endl;

    if (numToModify < 0 || numToModify >= container.size())
    {
        bad("Enter a valid number string number");
        return;
    }

    vector<string> menuItems = {
        "Change value",
        "Reverse",
        "Replace (given substring with another string)",
        "Remove excessive spaces",
        "Convert to uppercase",
        "Convert to lowercase",
        "Find substring",
        "Exit"};
    ll userDecision = showMenu(menuItems);
    cin.ignore();

    if (userDecision == 1)
    {
        string value;
        cout << "Enter new value: ";
        getline(cin, value);
        container[numToModify]->setValue(value);
    }
    else if (userDecision == 2)
    {
        container[numToModify]->m_reverse();
    }
    else if (userDecision == 3)
    {
        string replaceThis;
        string withThis;
        cout << "Enter substring to replace: ";
        getline(cin, replaceThis);
        cout << "Enter substring to replace with: ";
        getline(cin, withThis);
        container[numToModify]->m_replace(replaceThis, withThis);
    }
    else if (userDecision == 4)
    {
        container[numToModify]->m_remove_spaces();
    }
    else if (userDecision == 5)
    {
        container[numToModify]->m_to_upper();
    }
    else if (userDecision == 6)
    {
        container[numToModify]->m_to_lower();
    }
    else if (userDecision == 7)
    {
        string value;
        cout << "Enter substring: ";
        getline(cin, value);
        container[numToModify]->m_find_substring(value);
    }

    cout << endl;
    showStrings(container);
}

void outputMenu(vector<unique_ptr<DynamicString>> &container)
{
    vector<string> menuItems = {
        "Show strings",
        "Add strings",
        "Remove strings",
        "Modify strings",
        "Exit"};
    ll userDecision = showMenu(menuItems);

    if (userDecision == 1)
    {
        menuItems = {
            "Show in console",
            "Show in file",
            "Exit"};
        userDecision = showMenu(menuItems);

        if (userDecision == 1)
            showStrings(container);
        else if (userDecision == 2)
        {
            string fileName = getFileName();
            showStrings(container, fileName);
        }
    }
    else if (userDecision == 2)
    {
        menuItems = {
            "Add strings from file",
            "Add strings from console",
            "Exit"};
        userDecision = showMenu(menuItems);

        if (userDecision == 1)
            addStrings(container);
        else if (userDecision == 2)
        {
            string fileName = getFileName();
            addStrings(container, fileName);
        }
    }
    else if (userDecision == 3)
    {
        removeString(container);
    }
    else if (userDecision == 4)
    {
        modifyString(container);
    }
}