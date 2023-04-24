#include "sup.h"
#include "D:\repos\university\lib.h"

// Створити клас Delta таким чином, щоб кожний об’єкт вміщував свій персональний номер (дескриптор об’єкта) та функцію, яка повертає його значення. Дескриптор об’єкта – унікальне для об’єктів даного типу ціле число.
// Виконати завдання з лабораторної роботи №1, де тип елементу заданої структури даних довільний. Використати шаблонні функції.

template <typename T>
class Delta
{
private:
    ll descriptor;
    T value;

public:
    Delta() : value(), descriptor(nextDescriptor()) {}
    Delta(T inValue) : value(inValue), descriptor(nextDescriptor()) {}
    static ll nextDescriptor()
    {
        static ll nextDescriptor = 0;
        return nextDescriptor++;
    }
    T getValue() const { return value; }
    ll getDescriptor() const { return descriptor; }
    void setValue(T inValue) { value = inValue; }
    ~Delta() {}
};

template <typename T>
void createObjects(vector<unique_ptr<Delta<T>>> &deltaObjectsVector)
{
    cout << "\nEnter an amount of objects to create: ";
    ll objectsAmount = getNum();

    if (objectsAmount < 1)
    {
        cout << RED << "\nERROR: Invalid amount of objects...\n\n"
             << UNRED;
        return;
    }

    cout << "\nAdding objects (" << objectsAmount << "):\n";
    for (ll i = 0; i < objectsAmount; i++)
    {
        cin.ignore();
        T value;
        cout << i + 1 << ". Enter value for object: ";
        cin >> value;
        deltaObjectsVector.push_back(make_unique<Delta<T>>(value));
    }

    return;
}

template <typename T>
void printObjects(vector<unique_ptr<Delta<T>>> &deltaObjectsVector)
{
    ll vectorSize = deltaObjectsVector.size();
    if (vectorSize == 0)
    {
        bad("No objects to print");
        return;
    }

    cout << BOLD << "\nYour objects (" << vectorSize << "): \n"
         << UNBOLD;
    for (ll i = 0; i < vectorSize; i++)
    {
        cout << deltaObjectsVector[i]->getDescriptor() << ". " << deltaObjectsVector[i]->getValue() << endl;
    }
}

template <typename T>
void deleteObjects(vector<unique_ptr<Delta<T>>> &deltaObjectsVector)
{
    if (deltaObjectsVector.size() == 0)
        cout << GRAY << "\nNo objects to delete\n"
             << UNGRAY;
    else
    {
        printObjects(deltaObjectsVector);

        cout << "\nEnter a number of object to delete: ";
        ll numToDelete = getNum();

        if (numToDelete > deltaObjectsVector.size() - 1 || numToDelete < 0)
            cout << RED << "\nERROR: Invalid object number\n"
                 << UNRED;
        else
        {
            cout << GREEN << endl
                 << deltaObjectsVector[numToDelete]->getValue() << " successfully deleted\n"
                 << UNGREEN;

            deltaObjectsVector.erase(deltaObjectsVector.begin() + numToDelete);
        }
    }

    return;
}

template <typename T>
void outputMenu(vector<unique_ptr<Delta<T>>> &deltaObjectsVector)
{
    char doContinue;
    do
    {
        vector<string> menuItems = {
            "Add objects",
            "Delete objects",
            "Print objects",
            "Exit"};
        ll userDecision = showMenu(menuItems);

        if (userDecision == 1)
        {
            createObjects(deltaObjectsVector);
            printObjects(deltaObjectsVector);
        }
        else if (userDecision == 2)
        {
            deleteObjects(deltaObjectsVector);
            printObjects(deltaObjectsVector);
        }
        else if (userDecision == 3)
            printObjects(deltaObjectsVector);

        cout << "\nWould you like to return to menu? (Y | N): ";
        cin >> doContinue;
        if (doContinue == 'y' || doContinue == 'Y')
        {
            cout << endl;
            continue;
        }
        else
            break;
    } while (doContinue == 'y' || doContinue == 'Y');
}