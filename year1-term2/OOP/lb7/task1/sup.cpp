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
    T objectDescriptor;

public:
    // create default constructor function
    Delta() : objectDescriptor(getNextDefaultDescriptor()) {}

    // next identifier creator
    static ll getNextDefaultDescriptor()
    {
        // use static variable for tracking identifier
        static int descriptorHolder = 0;
        // return it to user
        return descriptorHolder++;
    }

    T getObjectDescriptor() const
    {
        return objectDescriptor;
    }

    // create default destructor function
    ~Delta()
    {
    }
};

// object creation function
template <typename T>
void createObjects(vector<unique_ptr<Delta<T>>> &deltaObjectsVector)
{
    // ask user to enter number of delta objects to create
    ll objectsAmount;
    cout << "\nEnter an amount of objects to create: ";
    cin >> objectsAmount;

    // if entered text is not an integer
    if (cin.fail())
    {
        // output error
        cout << RED << "\nERROR: Enter an integer...\n\n"
             << UNRED;
        // clear buffer
        cin.clear();
        cin.ignore();
        // stop function execution
        return;
    }
    // if entered amount is less than one
    else if (objectsAmount < 1)
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

        // prompt user to enter an object number to delete
        ll numToDelete = 0;
        cout << "\nEnter a number of object to delete: ";
        cin >> numToDelete;

        // check if entered text is not an integer
        if (cin.fail())
        {
            // output error
            cout << RED << "\nERROR: Enter an integer...\n\n"
                 << UNRED;
            // clear buffer
            cin.clear();
            cin.ignore();
            // stop function execution
            return;
        }

        // modify object number to fit in with indeces
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

template <typename T>
vector<unique_ptr<Delta<T>>> getTypeFromUser()
{
    cout << BOLD << "Choose a data type for a class\n"
         << UNBOLD;
    cout << "1. Integer\n";
    cout << "2. Double\n";
    cout << "3. String\n";
    cout << "4. Exit\n";
    cout << "\nEnter: ";
    ll inputType = getNum();
    cout << endl;

    if (inputType == 1)
        return vector<unique_ptr<Delta<int>>>();
    else if (inputType == 2)
        return vector<unique_ptr<Delta<double>>>();
    else
        return vector<unique_ptr<Delta<string>>>();
}