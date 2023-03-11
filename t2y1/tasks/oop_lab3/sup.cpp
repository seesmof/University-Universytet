#include <bits/stdc++.h>
#include "sup.h"
#include "../../../lib.h"
using namespace std;

// Варіант 5.Створити базовий клас Людина, відповідно до варіанту 4.
// Створити похідний клас Інженер, що містить додаткові дані: рік закінчення, ВУЗ, спеціальність, тип диплому, тип навчання, перекваліфікація (динамічний масив), місце роботи, заробітня платня.
// Клас повинен містити наступні методи: ініціалізації інформації, розрахунок заробітної платні, розрахунок щорічного доходу, додавання інформацій щодо перекваліфікації.
// Варіант 4.Створити базовий клас Людина. Кожний об’єкт класу повинен містити наступні дані: ПІБ, рік народження, стать.
// Клас повинен виконувати наступні дії: ініціалізація інформації, введення-виведення інформації.
// Створити похідний клас Студент, що має додаткові дані: рік вступу, № залікової книжки, кількість дисциплін що вивчається, дисципліни (динамічний масив), середній бал.
// Клас повинен виконувати наступні функції: ініціалізація інформації, додавання дисциплін, розрахунок середнього балу, виводити загальну інформацію про студента.

class Human
{
private:
    string fullName;
    ll birthYear;
    char gender;

public:
    Human() : fullName("UNKNOWN"), birthYear(0), gender('0') {}

    Human(string inputFullName, ll inputBirthYear, char inputGender) : fullName(inputFullName), birthYear(inputBirthYear), gender(inputGender) {}

    string getName() const
    {
        return fullName;
    }

    ll getYear() const
    {
        return birthYear;
    }

    char getGender() const
    {
        return gender;
    }

    void setName(string inputName)
    {
        fullName = inputName;
    }

    void setYear(ll inputYear)
    {
        birthYear = inputYear;
    }

    void setGender(char inputGender)
    {
        gender = inputGender;
    }
};

class Student : public Student
{
private:
    ll firstYear;
    ll recordBookNum;
    ll numOfSubjects;
    vector<pair<string, ll>> subjectsVector;
    ll GPA;

public:
    Student() : firstYear(NULL), recordBookNum(NULL), numOfSubjects(NULL), GPA(NULL) {}

    Student(ll inputFirstYear, ll inputRecordBookNum, ll inputNumOfSubjects, ll inputGPA) : firstYear(inputFirstYear), recordBookNum(inputRecordBookNum), numOfSubjects(inputNumOfSubjects), GPA(inputGPA), subjectsVector(fillSubjects(subjectsVector, numOfSubjects)) {}

    vector<pair<string, ll>> fillSubjects(vector<pair<string, ll>> &subjectsVector, ll numOfSubjects)
    {
        vector<pair<string, ll>> resultsHolder;
        ll subCounter = 1;
        for (ll i = 0; i < numOfSubjects; i++)
        {
            cout << i + 1 << "." << subCounter << ". Subject name: ";
        }
    }
};

// define the Stop struct, which represents a stop on the route
class Stop
{
private:
    string stopName;             // name of the stop
    double distanceFromPrevious; // distance from previous stop
    Stop *previousStop;          // pointer to previous stop in route
    Stop *nextStop;              // pointer to next stop in route
public:
    Stop() : stopName("UNKNOWN"), distanceFromPrevious(0), previousStop(NULL), nextStop(NULL) {}
    Stop(string stopName, double distanceFromPrevious) : stopName(stopName), distanceFromPrevious(distanceFromPrevious), previousStop(NULL), nextStop(NULL) {}
    ~Stop() {}
    string getStopName() const { return stopName; }
    double getDistance() const { return distanceFromPrevious; }
    Stop *getPreviousStop() const { return previousStop; }
    Stop *getNextStop() const { return nextStop; }
};

// define the Route class, which represents a route composed of stops
class Route
{
private:
    Stop *firstStop; // pointer to first stop in route
    Stop *lastStop;  // pointer to last stop in route
public:
    // constructor initializes empty route with head and tail set to nullptr
    Route() : firstStop(nullptr), lastStop(nullptr) {}

    // destructor deletes all stops in route
    ~Route()
    {
        Stop *currentStop = firstStop;
        while (currentStop != nullptr)
        {
            Stop *nextStop = currentStop->getNextStop();
            delete currentStop;
            currentStop = nextStop;
        }
    }

    Stop *getFirstStop() const
    {
        return firstStop;
    }

    Stop *getLastStop() const
    {
        return lastStop;
    }

    ll getStopsCount()
    {
        ll stopsCount = 0;
        Stop *currentStop = firstStop;
        while (currentStop != nullptr)
        {
            stopsCount++;
            currentStop = currentStop->getNextStop();
        }
        return stopsCount;
    }

    // adds a new stop with the given name and distance from previous stop to the end of the route
    void add_stop(string inputStopName, double inputDistance)
    {
        Stop *stopHolder = new Stop(inputStopName, inputDistance);

        if (lastStop == nullptr)
        {
            firstStop = stopHolder;
            lastStop = stopHolder;
        }
        else
        {
            stopHolder->getPreviousStop() = lastStop;
            lastStop->nextStop = stopHolder;
            lastStop = stopHolder;
        }
    }

    // returns the length of the route by summing the distance between each pair of adjacent stops
    double len_route()
    {
        double totalLength = 0.0;
        Stop *currentStopHolder = firstStop;
        while (currentStopHolder != nullptr)
        {
            totalLength += currentStopHolder->distanceFromPrevious;
            currentStopHolder = currentStopHolder->nextStop;
        }
        return totalLength;
    }

    // returns the time required to travel the route assuming a fixed speed of 50 km/h
    double time_route()
    {
        double routeTime = len_route() / 50.0;
        return routeTime;
    }
};

// printing objects function
void showRoute(Route &routeContainer)
{
    // get vector size
    ll routeSize = routeContainer.getStopsCount();
    if (routeSize == 0)
    {
        cout << GRAY << "No stops found yet...\n"
             << UNGRAY;
        return;
    }
    // output all objects with their identifiers using a for loop
    cout << BOLD << "\nStops (" << routeSize << "): \n"
         << UNBOLD;
    ll counter = 1;
    ll subCounter = 1;
    Stop *stopHolder = routeContainer.getFirstStop();
    while (stopHolder != NULL)
    {
        // output student's name and age
        cout << counter << "." << subCounter << ". Name: " << stopHolder->stopName << endl;
        subCounter++;
        cout << counter << "." << subCounter << ". Distance: " << stopHolder->distanceFromPrevious << endl
             << endl;
        stopHolder = stopHolder->nextStop;
        counter++;
        subCounter = 1;
    }
    // end function execution
    return;
}

// object creation function
void addStop(Route &routeContainer)
{
    // ask user to enter number of Stud objects to create
    cout << "\nEnter an amount of stops to add: ";
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
    for (ll counter = 1; counter <= objectsAmount; counter++)
    {
        cin.ignore();
        string stopName;
        cout << counter << "." << subCounter << ". Enter stop name: ";
        getline(cin, stopName);
        stopName = validateName(stopName);
        subCounter++;

        cout << counter << "." << subCounter << ". Enter distance: ";
        double distanceFromPreviousStop = getNum();

        routeContainer.add_stop(stopName, distanceFromPreviousStop);
        subCounter = 1;
    }
    // end function execution
    return;
}

// // for calculating student age
// ll calculateStudentAge(unique_ptr<Stud> &StudentObject)
// {
//     // get student's birth year and current year
//     ll birthYear = StudentObject->getStudentBirthYear();
//     const ll CURRENT_YEAR = 2023;
//     // calcualte student's age by subtracting their birth year from current year
//     ll studentAge = CURRENT_YEAR - birthYear;
//     // return student's age
//     return studentAge;
// }

// // for editing student information
// void editStudent(vector<unique_ptr<Stud>> &studentVector)
// {
//     // get student's nubmer
//     cout << "Enter student number: ";
//     // validate student number
//     ll studentNumberHolder = getNum();
//     // fit it into the vector indeces
//     studentNumberHolder--;
//     // check if the number is within the range
//     if (studentNumberHolder < 0 || studentNumberHolder > studentVector.size())
//     {
//         // if not output the error message
//         cout << RED << "\nERROR: No such student number exists...\n\n"
//              << UNRED;
//         // and stop the function execution
//         return;
//     }
//     // if all validation was successful output the menu
//     cout << BOLD << "\nWhat property would you like to edit?\n"
//          << UNBOLD;
//     cout << "1. Name\n";
//     cout << "2. Birth Year\n";
//     cout << "Enter: ";
//     // and ask the user to make a choice
//     ll userChoice = getNum();
//     cout << endl;
//     // if user chose to edit the name
//     if (userChoice == 1)
//     {
//         // ask user to enter new student name
//         string studentName;
//         cout << "Enter student name: ";
//         getline(cin, studentName);
//         // validate it
//         studentName = validateName(studentName);
//         // and modify the value
//         studentVector[studentNumberHolder]->setStudentName(studentName);
//         cout << GREEN << studentVector[studentNumberHolder]->getStudentName() << " name updated\n"
//              << UNGREEN;
//     }
//     // if user chose to edit the birth year
//     else if (userChoice == 2)
//     {
//         // ask user to enter new birth year
//         cout << "Enter student's birth year: ";
//         // validate it
//         ll studentYear = getNum();
//         // modify the value
//         studentVector[studentNumberHolder]->setStudentBirthYear(studentYear);
//         cout << GREEN << studentVector[studentNumberHolder]->getStudentName() << " birth year updated\n"
//              << UNGREEN;
//     }
//     // stop function execution
//     return;
// }

// // object deletion function
// void deleteStudent(vector<unique_ptr<Stud>> &studentVector)
// {
//     // check if vector is empty
//     if (studentVector.size() == 0)
//         // if so, output error message
//         cout << GRAY << "\nNo objects to delete\n"
//              << UNGRAY;
//     // if not
//     else
//     {
//         // print all objects to user
//         showStudents(studentVector);
//         // prompt user to enter an object number to delete
//         cout << "\nEnter a student nubmer to delete: ";
//         ll studentNumber = getNum();
//         // modify object number to fit in with indeces
//         studentNumber--;
//         // if the object number is out of range
//         if (studentNumber > studentVector.size() - 1 || studentNumber < 0)
//             // output error message
//             cout << RED << "\nERROR: Invalid student number...\n\n"
//                  << UNRED;
//         // if not
//         else
//         {
//             // output success message
//             cout << GREEN << endl
//                  << studentVector[studentNumber]->getStudentName() << " successfully deleted\n"
//                  << UNGREEN;
//             // erase object from vector
//             studentVector.erase(studentVector.begin() + studentNumber);
//         }
//     }
//     // end function execution
//     return;
// }

// for showing the main menu of the application
void outputMenu(Route &routeContainer)
{
    // output the menu
    cout << BOLD << "Welcome! Choose some option from below\n"
         << UNBOLD;
    cout << "1. Show route\n";
    cout << "2. Add stop\n";
    cout << "3. Remove stop\n";
    cout << "4. Show route length\n";
    cout << "5. Show route time\n";
    // ask user to enter their choice
    cout << "Enter: ";
    // and validate it
    ll userDecision = getNum();
    cout << endl;

    // create a switch statement
    switch (userDecision)
    {
    case 1:
        showRoute(routeContainer);
        break;
    case 2:
        showRoute(routeContainer);
        addStop(routeContainer);
        break;
    case 3:
        break;
    case 4:
        break;
    default:
        return;
    }
}