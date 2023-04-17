#include "sup.h"
#include "D:\repos\university\lib.h"

// Створити клас Delta таким чином, щоб кожний об’єкт вміщував свій персональний номер (дескриптор об’єкта) та функцію, яка повертає його значення. Дескриптор об’єкта – унікальне для об’єктів даного типу ціле число.
// Виконати завдання з лабораторної роботи №1, де тип елементу заданої структури даних довільний. Використати шаблонні функції.

// delta class declaration
template <typename T>
class Delta
{
private:
    // declare private members
    ll descriptor;
    T value;

public:
    // create default constructor function
    Delta(T inValue) : value(inValue), descriptor(nextDescriptor()) {}

    static ll nextDescriptor()
    {
        static ll nextDescriptor = 0;
        return nextDescriptor++;
    }

    // next identifier creator
    T getValue() const
    {
        return value;
    }

    ll getDescriptor() const
    {
        return descriptor;
    }

    // create default destructor function
    ~Delta()
    {
    }
};
template <typename T>
ll Delta<T>::nextDescriptor = 0;

// object creation function
template <typename T>
void createObjects(vector<unique_ptr<Delta<T>>> &deltaObjectsVector)
{
    // ask user to enter number of delta objects to create
    cout << "\nEnter an amount of objects to create: ";
    ll objectsAmount = getNum();

    // if entered amount is less than one
    if (objectsAmount < 1)
    {
        // output error and stop function
        cout << RED << "\nERROR: Invalid amount of objects...\n\n"
             << UNRED;
        // stop function execution
        return;
    }

    // create specified amount of objects using a for loop
    for (ll i = 0; i < objectsAmount; i++)
        deltaObjectsVector.push_back(make_unique<Delta<T>>());

    // end function execution
    return;
}

// printing objects function
template <typename T>
void printObjects(vector<unique_ptr<Delta<T>>> &deltaObjectsVector)
{
    // get vector size
    ll vectorSize = deltaObjectsVector.size();

    // output all objects with their identifiers using a for loop
    cout << BOLD << "\nYour objects (" << vectorSize << "): \n"
         << UNBOLD;
    for (ll i = 0; i < vectorSize; i++)
        cout << i + 1 << ". Descriptor: " << deltaObjectsVector[i]->getObjectDescriptor() << endl;

    // end function execution
    return;
}

// object deletion function
template <typename T>
void deleteObjects(vector<unique_ptr<Delta<T>>> &deltaObjectsVector)
{
    // check if vector is empty
    if (deltaObjectsVector.size() == 0)
        // if so, output error message
        cout << GRAY << "\nNo objects to delete\n"
             << UNGRAY;
    // if not
    else
    {
        // print all objects to user
        printObjects(deltaObjectsVector);

        cout << "\nEnter a number of object to delete: ";
        ll numToDelete = getNum();
        numToDelete--;

        // if the object number is out of range
        if (numToDelete > deltaObjectsVector.size() - 1 || numToDelete < 0)
            // output error message
            cout << RED << "\nERROR: Invalid object number\n"
                 << UNRED;
        // if not
        else
        {
            // output success message
            cout << GREEN << endl
                 << deltaObjectsVector[numToDelete]->getObjectDescriptor() << " successfully deleted\n"
                 << UNGREEN;

            // erase object from vector
            deltaObjectsVector.erase(deltaObjectsVector.begin() + numToDelete);
        }
    }

    // end function execution
    return;
}

// for showing the main menu of the application
template <typename T>
void outputMenu(vector<Delta<T>> &container)
{
    // output menu to user and prompt them to choose an option
    cout << BOLD << "Choose an option from menu\n"
         << UNBOLD;
    cout << "1. Add objects\n";
    cout << "2. Delete objects\n";
    cout << "3. Print objects\n";
    cout << "4. Exit\n";
    cout << "\nEnter: ";
    userDecision = getNum();
    cout << endl;

    // if user chose to add objects
    if (userDecision == 1)
    {
        vector<unique_ptr<Delta<T>>> deltaObjectsVector;
        // add objects
        createObjects(deltaObjectsVector);
        // print them to console
        printObjects(deltaObjectsVector);
    }
    // if user chose to delete objects
    else if (userDecision == 2)
    {
        // delete them
        deleteObjects(deltaObjectsVector);
        // print them to console
        printObjects(deltaObjectsVector);
    }
    // if user chose to print objects
    else if (userDecision == 3)
        // print objects to console
        printObjects(deltaObjectsVector);
}