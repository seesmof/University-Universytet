#include <bits/stdc++.h>
#include "sup.h"
#include "../../../lib.h"
using namespace std;

// delta class declaration
class Delta
{
private:
    // declare private members
    ll objectDescriptor;

public:
    // create default constructor function
    Delta() : objectDescriptor(getNextDefaultDescriptor()) {}
    Delta(const ll objectDescriptor) : objectDescriptor(objectDescriptor) {}

    // next identifier creator
    static ll getNextDefaultDescriptor()
    {
        // use static variable for tracking identifier
        static int descriptorHolder = 0;
        // return it to user
        return descriptorHolder++;
    }

    // getter for object identifier
    ll getObjectDescriptor() const
    {
        return objectDescriptor;
    }

    // create default destructor function
    ~Delta() {}
};

bool validateDescriptor(ll descriptorHolder, vector<unique_ptr<Delta>> &deltaObjectsVector)
{
    for (const auto &delta : deltaObjectsVector)
    {
        if (delta->getObjectDescriptor() == descriptorHolder)
        {
            return false;
        }
    }
    return true;
}

// object creation function
void createObjects(vector<unique_ptr<Delta>> &deltaObjectsVector)
{
    ll userDecision;
    cout << BOLD << "\nHow would you like to add objects?\n"
         << UNBOLD;
    cout << "1. Enter manually\n";
    cout << "2. Generate automatically\n";
    cout << "3. Exit\n";
    cin >> userDecision;
    cout << endl;

    // ask user to enter number of delta objects to create
    ll objectsAmount;
    cout << "\nEnter an amount of objects to create: ";
    cin >> objectsAmount;

    // if entered amount is less than one
    if (objectsAmount < 1)
    {
        // output error and stop function
        cout << RED << "\nERROR: Invalid amount of objects...\n\n"
             << UNRED;
        return;
    }

    if (userDecision == 1)
    {
        cout << BOLD << "How would you like to get objects?\n"
             << UNBOLD;
        cout << "1. Enter one-by-one from keyboard\n";
        cout << "2. Enter from file\n";
        cout << "3. Exit\n";
        cin >> userDecision;
        cout << endl;

        if (userDecision == 1)
        {
            // create objects
            for (ll i = 0; i < objectsAmount; i++)
            {
                ll descriptorHolder;
                cout << i + 1 << ". Enter: ";
                cin >> descriptorHolder;

                bool isUnique = validateDescriptor(descriptorHolder, deltaObjectsVector);

                if (isUnique == false)
                {
                    cout << RED << "\nERROR: Object descriptor is not unique...\n\n"
                         << UNRED;
                    continue;
                }
                else
                    deltaObjectsVector.push_back(make_unique<Delta>(descriptorHolder));
            }
        }
    }

    // create specified amount of objects using a for loop
    for (ll i = 0; i < objectsAmount; i++)
    {
        deltaObjectsVector.push_back(make_unique<Delta>());
    }

    // end function execution
    return;
}

// printing objects function
void printObjects(vector<unique_ptr<Delta>> &deltaObjectsVector)
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
void deleteObjects(vector<unique_ptr<Delta>> &deltaObjectsVector)
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