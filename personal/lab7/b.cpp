// include necessary libraries
#include <bits/stdc++.h>
using namespace std;

// create a structure to hold the semi truck's information
struct futureStudent
{
    // declare variables for storing Прізвище Ім'я По-батькові
    string P;
    string I;
    string B;
    // declare variable for storing age
    int age;
    // declare variable for storing school GPA
    double schoolGPA;
    // declare variables for storing NMT results and additional scores
    int resultNMT[3];
    double additionalScore;
    // declare variable for storing whether the student has originals of documents
    bool hasOriginalDocs;
    // declare variables for storing university name and specialization
    string universityName;
    string specialization;
    // declare variables for storing total and average NMT scores
    double totalNMTscore;
    double averageNMTscore;
};

struct places
{
    int competitivePlacesCount;
};

// declare function prototypes
void studentInput(int n, futureStudent *student, places *place);
void studentSearch(int n, futureStudent *student);

// declare main function
int main(int argc, char **argv)
{
    cout << endl;
    ////////////////////////////////////////////////////////////////////////////

    // ask user to enter the amount of students
    int n;
    cout << "Enter the amount of students you want to enter: ";
    cin >> n;

    // declare 1d array with students' information of N size
    futureStudent student[n];
    places place[n];

    // call a function for students' data input
    studentInput(n, student, place);

    sort(student, student + n);
    reverse(student, student + n);

    for (int i = 0; i < n; i++)
        cout << student[i].P << " - " << student[i].resultNMT[0] << " " << student[i].resultNMT[1] << student[i].resultNMT[2] << endl;

    ////////////////////////////////////////////////////////////////////////////
    cout << endl;
    return 0;
}

// create function that will ask user to input information for each of the vehicles
void studentInput(int n, futureStudent *student, places *place)
{
    // create a local variable for storing user's answer to yes/no questions
    char confirmation;
    // create for loop for looping through an array and asking user to input each student's data
    for (int i = 0; i < n; i++)
    {
        // declare local variable for storing the result number
        int subCount = 1;

        // ask user to enter student's ПІБ
        cout << endl;
        cout << i + 1 << "." << subCount << " Enter student's PIB: ";
        cin >> (student + i)->P >> student[i].I >> student[i].B;
        // create 3 functions for converting first lowercase letters of students name to uppercase
        if (islower(student[i].P[0]))
        {
            student[i].P[0] = toupper(student[i].P[0]);
        }
        if (islower(student[i].I[0]))
        {
            student[i].I[0] = toupper(student[i].I[0]);
        }
        if (islower(student[i].B[0]))
        {
            student[i].B[0] = toupper(student[i].B[0]);
        }
        subCount++;

        // ask user to enter student's age
        cout << i + 1 << "." << subCount << " Enter student's age: ";
        cin >> student[i].age;
        subCount++;

        // ask user to enter student's school GPA
        cout << i + 1 << "." << subCount << " Enter student's school GPA: ";
        cin >> student[i].schoolGPA;
        subCount++;

        // ask user to enter student's NMT results
        cout << i + 1 << "." << subCount << " Enter student's NMT results (1 2 3): ";
        cin >> student[i].resultNMT[0] >> student[i].resultNMT[1] >> student[i].resultNMT[2];
        subCount++;

        // ask user to enter student's additional scores
        cout << i + 1 << "." << subCount << " Enter student's additional scores: ";
        cin >> student[i].additionalScore;
        subCount++;

        // ask user to enter if student has originals of documents or not
        cout << i + 1 << "." << subCount << " Does the student has the originals of all the documents? (Y / N): ";
        cin >> confirmation;
        // if the input == Y
        if (confirmation == 'y' || confirmation == 'Y')
        {
            // assign true value
            student[i].hasOriginalDocs = true;
        }
        // in any other cases
        else
        {
            // assign false value
            student[i].hasOriginalDocs = false;
        }
        subCount++;

        // ask user to enter student's university
        cout << i + 1 << "." << subCount << " Enter university this student will be going to: ";
        cin >> student[i].universityName;
        subCount++;

        int uni = 0;
        for (int j = 0; j < n; j++)
            if (student[j].universityName == student[i].universityName)
                uni++;

        // ask user to enter student's specialization
        cout << i + 1 << "." << subCount << " Enter the future specialization of the student: ";
        cin >> student[i].specialization;
        subCount++;

        int spec = 0;
        for (int j = 0; j < n; j++)
            if (student[j].specialization == student[i].specialization)
                spec++;

        if (spec < 2 && uni < 2)
        {
            cout << i + 1 << "." << subCount << " Enter number of competitive places for " << student[i].specialization << " at " << student[i].universityName << ": ";
            cin >> place[i].competitivePlacesCount;
        }

        // calculate total NMT score by combining three inputted NMT results and multiply them by additional score
        student[i].totalNMTscore = (student[i].resultNMT[0] + student[i].resultNMT[1] + student[i].resultNMT[2]) * student[i].additionalScore;
        // calculate average NMT score by dividing the total score by the amount of scores, 3 in our case
        student[i].averageNMTscore = student[i].totalNMTscore / 3;

        // output student's total and average scores
        cout << student[i].I << " has a total score of " << student[i].totalNMTscore << " and an average score of " << student[i].averageNMTscore << "." << endl;

        // create a function for calculating the amount of students who have the same university and specialization inputted
        // declare local variable for storing student count
        int studentCount = 0;
        // declare variable for storing global average score
        double globalAvgScore = 0.0;
        // create for loop for iterating through an array
        for (int j = 0; j < n; j++)
        {
            // if we are on the first iteration
            if (i == 0)
            {
                // skip iteration
                continue;
            }
            // in any other cases
            else
            {
                // if we are on the same iteration as we just inputed
                if (j == i)
                {
                    // skip iteration
                    continue;
                }
                // in any other cases
                else
                {
                    // if students' univesities and specialization match
                    if (student[i].universityName == student[j].universityName && student[i].specialization == student[j].specialization)
                    {
                        // increase counter
                        studentCount++;
                        // add this student's NMT score to global average
                        globalAvgScore += student[j].averageNMTscore;
                    }
                }
            }
        }
        // divide global average score by student count to get the average
        globalAvgScore /= studentCount;

        // if student count > 0
        if (studentCount > 0)
        {
            // output the amount of students found
            cout << endl;
            cout << "There are " << studentCount << " students who are going to the same University." << endl;
            // and their average score
            cout << "Their average score is " << globalAvgScore << endl;
        }
    }
    // end function
    return;
}