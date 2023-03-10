#include <bits/stdc++.h>
#include "sup.h"
#include "../../../lib.h"
using namespace std;

// Розробити клас Stud, Який містить інформацію про ім'я студента, рік його народження. Передбачити: можливість автоматичної нумерації створених оь'єктів класу, ініціалізацію об'єктів пустими параметрами та параметрами визначеними зазделагідь, можливість запису та зчитування полів класу із-зовні, встановлення полів об'єкту із запитом до користувача та через передані дані, виведення всієї інформації на екран, зміну параметрів об'єкта, дружню функцію для підрахунку віку студента.

// Stud class declaration
class Stud
{
private:
    // create private member variables
    ll studentNumber;
    string studentName;
    ll studentBirthYear;

public:
    // create default constructor function
    Stud()
    {
        studentNumber = getNextStudentNumber();
        studentName = "UNKNOWN";
        studentBirthYear = 0;
    }
    // create parameterized constructor
    Stud(string inputStudentName, ll inputStudentBirthYear)
    {
        // take parameters and set class variables to them
        studentNumber = getNextStudentNumber();
        studentName = inputStudentName;
        studentBirthYear = inputStudentBirthYear;
    }
    // for handling student number
    static ll getNextStudentNumber()
    {
        static ll studentNumberHolder = 0;
        return studentNumberHolder++;
    }
    // student number getter
    ll getStudentNumber() const
    {
        return studentNumber;
    }
    // student name getter
    string getStudentName() const
    {
        return studentName;
    }
    // student birth year getter
    ll getStudentBirthYear() const
    {
        return studentBirthYear;
    }
    // student name setter
    void setStudentName(string inputStudentName)
    {
        studentName = inputStudentName;
    }
    // student birth year setter
    void setStudentBirthYear(ll inputStudentBirthYear)
    {
        studentBirthYear = inputStudentBirthYear;
    }
    // declare calculateStudentAge function as friend
    friend void calculateStudentAge(Stud);
    // create default destructor function
    ~Stud()
    {
    }
};

// for calculating student age
ll calculateStudentAge(unique_ptr<Stud> &StudentObject)
{
    // get student's birth year and current year
    ll birthYear = StudentObject->getStudentBirthYear();
    const ll CURRENT_YEAR = 2023;
    // calcualte student's age by subtracting their birth year from current year
    ll studentAge = CURRENT_YEAR - birthYear;
    // return student's age
    return studentAge;
}

// object creation function
void addStudents(vector<unique_ptr<Stud>> &studentVector)
{
    // ask user to enter number of Stud objects to create
    cout << "\nEnter an amount of students to add: ";
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
    cout << endl;
    ll subCounter = 1;
    for (ll i = 0; i < objectsAmount; i++)
    {
        // ask user to enter student's name and validate it
        cin.ignore();
        string studentNameHolder;
        cout << i + 1 << "." << subCounter << ". Enter student's name: ";
        getline(cin, studentNameHolder);
        studentNameHolder = validateName(studentNameHolder);
        subCounter++;
        // ask user to enter student's birth year and validate it as well
        cout << i + 1 << "." << subCounter << ". Enter student's birth year: ";
        ll birthYearHolder = getNum();
        // make a new student object and add it to the vector
        studentVector.eb(make_unique<Stud>(studentNameHolder, birthYearHolder));
        cout << endl;
        subCounter = 1;
    }
    // end function execution
    return;
}

// printing objects function
void showStudents(vector<unique_ptr<Stud>> &studentVector)
{
    // get vector size
    ll vectorSize = studentVector.size();
    // output all objects with their identifiers using a for loop
    cout << BOLD << "\nStudents (" << vectorSize << "): \n"
         << UNBOLD;
    ll subCounter = 1;
    for (ll i = 0; i < vectorSize; i++)
    {
        // output student's name and age
        cout << i + 1 << "." << subCounter << ". Name: " << studentVector[i]->getStudentName() << endl;
        subCounter++;
        cout << i + 1 << "." << subCounter << ". Age: " << calculateStudentAge(studentVector[i]) << endl
             << endl;
        subCounter = 1;
    }
    // end function execution
    return;
}

// for editing student information
void editStudent(vector<unique_ptr<Stud>> &studentVector)
{
    // get student's nubmer
    cout << "Enter student number: ";
    // validate student number
    ll studentNumberHolder = getNum();
    // fit it into the vector indeces
    studentNumberHolder--;
    // check if the number is within the range
    if (studentNumberHolder < 0 || studentNumberHolder > studentVector.size())
    {
        // if not output the error message
        cout << RED << "\nERROR: No such student number exists...\n\n"
             << UNRED;
        // and stop the function execution
        return;
    }
    // if all validation was successful output the menu
    cout << BOLD << "\nWhat property would you like to edit?\n"
         << UNBOLD;
    cout << "1. Name\n";
    cout << "2. Birth Year\n";
    cout << "Enter: ";
    // and ask the user to make a choice
    ll userChoice = getNum();
    cout << endl;
    // if user chose to edit the name
    if (userChoice == 1)
    {
        // ask user to enter new student name
        string studentName;
        cout << "Enter student name: ";
        getline(cin, studentName);
        // validate it
        studentName = validateName(studentName);
        // and modify the value
        studentVector[studentNumberHolder]->setStudentName(studentName);
        cout << GREEN << studentVector[studentNumberHolder]->getStudentName() << " name updated\n"
             << UNGREEN;
    }
    // if user chose to edit the birth year
    else if (userChoice == 2)
    {
        // ask user to enter new birth year
        cout << "Enter student's birth year: ";
        // validate it
        ll studentYear = getNum();
        // modify the value
        studentVector[studentNumberHolder]->setStudentBirthYear(studentYear);
        cout << GREEN << studentVector[studentNumberHolder]->getStudentName() << " birth year updated\n"
             << UNGREEN;
    }
    // stop function execution
    return;
}

// object deletion function
void deleteStudent(vector<unique_ptr<Stud>> &studentVector)
{
    // check if vector is empty
    if (studentVector.size() == 0)
        // if so, output error message
        cout << GRAY << "\nNo objects to delete\n"
             << UNGRAY;
    // if not
    else
    {
        // print all objects to user
        showStudents(studentVector);
        // prompt user to enter an object number to delete
        cout << "\nEnter a student nubmer to delete: ";
        ll studentNumber = getNum();
        // modify object number to fit in with indeces
        studentNumber--;
        // if the object number is out of range
        if (studentNumber > studentVector.size() - 1 || studentNumber < 0)
            // output error message
            cout << RED << "\nERROR: Invalid student number...\n\n"
                 << UNRED;
        // if not
        else
        {
            // output success message
            cout << GREEN << endl
                 << studentVector[studentNumber]->getStudentName() << " successfully deleted\n"
                 << UNGREEN;
            // erase object from vector
            studentVector.erase(studentVector.begin() + studentNumber);
        }
    }
    // end function execution
    return;
}

// for showing the main menu of the application
void outputMenu(vector<unique_ptr<Stud>> &studentVector)
{
    // output the menu
    cout << BOLD << "Welcome! Choose some option from below\n"
         << UNBOLD;
    cout << "1. Add students\n";
    cout << "2. Show students\n";
    cout << "3. Edit students\n";
    cout << "4. Delete students\n";
    // ask user to enter their choice
    cout << "Enter: ";
    // and validate it
    ll userDecision = getNum();
    cout << endl;

    // create a switch statement
    switch (userDecision)
    {
    case 1:
        showStudents(studentVector);
        addStudents(studentVector);
        break;
    case 2:
        showStudents(studentVector);
        break;
    case 3:
        editStudent(studentVector);
        break;
    case 4:
        showStudents(studentVector);
        deleteStudent(studentVector);
        break;
    default:
        return;
    }
}