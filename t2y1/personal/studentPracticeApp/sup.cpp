#include <bits/stdc++.h>
#include "sup.h"
#include "../../../lib.h"
using namespace std;

// Stud class declaration
class Stud
{
private:
    static ll studentNumber;
    string studentName;
    ll studentBirthYear;

public:
    // create default constructor function
    Stud()
    {
        ++studentNumber;
        studentName = "UNKNOWN";
        studentBirthYear = 0;
    }

    Stud(string inputStudentName, ll inputStudentBirthYear)
    {
        ++studentNumber;
        studentName = inputStudentName;
        studentBirthYear = inputStudentBirthYear;
    }

    ll getStudentNumber() const
    {
        return studentNumber;
    }

    string getStudentName() const
    {
        return studentName;
    }

    ll getStudentBirthYear() const
    {
        return studentBirthYear;
    }

    void getStudent()
    {
        cout << studentNumber << ". Name: " << studentName << endl;
        cout << studentNumber << ". Birth Year: " << studentBirthYear << endl;
    }

    // next identifier creator
    static ll getNextDefaultDescriptor()
    {
        // use static variable for tracking identifier
        static int descriptorHolder = 0;
        // return it to user
        return descriptorHolder++;
    }

    ll getObjectDescriptor() const;

    // create default destructor function
    ~Stud()
    {
    }
};

// object creation function
void createObjects(vector<unique_ptr<Stud>> &StudObjectsVector)
{
    // ask user to enter number of Stud objects to create
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
        StudObjectsVector.push_back(make_unique<Stud>());

    // end function execution
    return;
}

// printing objects function
void printObjects(vector<unique_ptr<Stud>> &StudObjectsVector)
{
    // get vector size
    ll vectorSize = StudObjectsVector.size();

    // output all objects with their identifiers using a for loop
    cout << BOLD << "\nYour objects (" << vectorSize << "): \n"
         << UNBOLD;
    for (ll i = 0; i < vectorSize; i++)
        cout << i + 1 << ". Descriptor: " << StudObjectsVector[i]->getObjectDescriptor() << endl;

    // end function execution
    return;
}

// object deletion function
void deleteObjects(vector<unique_ptr<Stud>> &StudObjectsVector)
{
    // check if vector is empty
    if (StudObjectsVector.size() == 0)
        // if so, output error message
        cout << GRAY << "\nNo objects to delete\n"
             << UNGRAY;
    // if not
    else
    {
        // print all objects to user
        printObjects(StudObjectsVector);

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
        if (numToDelete > StudObjectsVector.size() - 1 || numToDelete < 0)
            // output error message
            cout << RED << "\nERROR: Invalid object number\n"
                 << UNRED;
        // if not
        else
        {
            // output success message
            cout << GREEN << endl
                 << StudObjectsVector[numToDelete]->getObjectDescriptor() << " successfully deleted\n"
                 << UNGREEN;

            // erase object from vector
            StudObjectsVector.erase(StudObjectsVector.begin() + numToDelete);
        }
    }

    // end function execution
    return;
}