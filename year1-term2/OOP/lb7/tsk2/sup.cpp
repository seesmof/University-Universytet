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
    void reverse()
    {
        string temp = m_value;
        reverse(temp.begin(), temp.end());
    }

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
        cout << i + 1 << ". " << container[i]->getValue() << " - " << container[i]->getSize() << endl;
    }
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

void outputMenu(vector<unique_ptr<DynamicString>> &container)
{
    vector<string> menuItems = {
        "1. Show strings",
        "2. Add strings",
        "3. Remove strings",
        "4. Exit"};
    ll userDecision = showMenu(menuItems);

    if (userDecision == 1)
    {
        showStrings(container);
    }
    else if (userDecision == 2)
    {
        addStrings(container);
    }
    else if (userDecision == 3)
    {
        removeString(container);
    }
}