#include "D:\repos\university\lib.h"
#include "sup.h"

// Виконати завдання з лабораторної роботи #1 використавши, для зберігання даних класи Standard Template Library (STL) або list або vector. Поясніть різницю в використанні цих класів.

class Delta
{
private:
public:
};

void createObjects(vector<unique_ptr<Delta>> &deltaObjectsVector)
{
}

void printObjects(vector<unique_ptr<Delta>> &deltaObjectsVector)
{
}

void deleteObjects(vector<unique_ptr<Delta>> &deltaObjectsVector)
{
}

void outputMenu(vector<unique_ptr<Delta>> &container)
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