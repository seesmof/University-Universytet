// include necessary libraries
#include <bits/stdc++.h>
using namespace std;

struct studentsData
{
    // declare variables for storing Прізвище Ім'я По-батькові
    string P;
    string I;
    string B;
    // declare variables for storing NMT results and additional scores
    int resultNMT[3];
    double additionalScore[3];
    // declare variables for storing university name and specialization
    string universityName;
    string specialization;
    // declare variables for storing total NMT score
    double totalNMTscore;
};

// function prototypes //
string randString(int);
string fileNameInput();
int countStudents(const string &);
void fillArr(studentsData *, int, const string &);
void fillArr(studentsData *, int);
void showStudents(studentsData *, int);
/////////////////////////

// func main start
int main()
{
    // declare local variables //
    srand(time(NULL));
    char doContinue;
    int userDecision;
    int numOfStudents;
    string inputFileName;
    /////////////////////////////

    // project intro
    cout << "\n/////////////////////////////////////////////////////////////\n"
         << "\nWelcome! This is a Task B from Lab 7\n"
         << "\n/////////////////////////////////////////////////////////////\n\n";
    do
    {
        //////////////////////////////////////////////////////////////////////////////////

        // ask user if input from file or by command line
        cout << "Would you like to enter students from file or by command line?\n";
        cout << "1 for file | 2 for command line |: ";
        cin >> userDecision;

        if (userDecision == 1)
        {
            cout << endl;
            // create variable for storing students information
            // inputFileName = fileNameInput();
            inputFileName = "data.txt";
            numOfStudents = countStudents(inputFileName);
        }
        else
        {
            cout << endl;
            cout << "Please enter the number of students: ";
            cin >> numOfStudents;
        }

        studentsData student[numOfStudents];

        if (userDecision == 1)
            fillArr(student, numOfStudents, inputFileName);
        else
            fillArr(student, numOfStudents);

        vector<double> scores(numOfStudents);
        for (int i = 0; i < numOfStudents; i++)
            scores.at(i) = student[i].totalNMTscore;

        vector<string> unis(numOfStudents);
        vector<string> places;
        for (int i = 0; i < numOfStudents; i++)
        {
            for (int j = i + 1; j < numOfStudents; j++)
            {
                if (student[i].universityName == student[j].universityName)
                    continue;
                else
                {
                    string buf = student[i].universityName;
                    cout << "Enter how many places are available for " << buf << ": ";
                    cin >> unis[i];
                }
            }
        }

        //////////////////////////////////////////////////////////////////////////////////
        cout << "\n/////////////////////////////////////////////////////////////\n"
             << "\nWould you like to continue program execution? (Y | N): ";
        cin >> doContinue;
        if (doContinue == 'Y' || doContinue == 'y')
        {
            cout << "\n/////////////////////////////////////////////////////////////\n\n";
            continue;
        }
        else
            break;
    } while (doContinue = 'Y' || doContinue == 'y');

    // func main end
    cout << "\nThanks for using this program\n"
         << "\n/////////////////////////////////////////////////////////////\n\n";
    return 0;
}

void showStudents(studentsData *arr, int n)
{
    cout << "Students List: \n";
    int addC = 1;
    for (int i = 0; i < n; i++)
    {
        addC = 1;

        cout << i + 1 << "." << addC << " PIB: " << arr[i].P << " " << arr[i].I << " " << arr[i].B << endl;
        addC++;

        cout << i + 1 << "." << addC << " NMT: " << arr[i].resultNMT[0] << " " << arr[i].resultNMT[1] << " " << arr[i].resultNMT[2] << endl;
        addC++;

        cout << i + 1 << "." << addC << " Additional score: " << arr[i].additionalScore[0] << " " << arr[i].additionalScore[1] << " " << arr[i].additionalScore[2] << endl;
        addC++;

        cout << i + 1 << "." << addC << " University name: " << arr[i].universityName << endl;
        addC++;

        cout << i + 1 << "." << addC << " Specialization: " << arr[i].specialization << endl;
        addC++;

        cout << i + 1 << "." << addC << " Total NMT score: " << arr[i].totalNMTscore << endl;
        addC++;

        cout << endl;
    }
}

void fillArr(studentsData *arr, int n)
{
    int addC = 1;
    for (int i = 0; i < n; i++)
    {
        addC = 1;

        cout << i + 1 << "." << addC << " Enter PIB: ";
        cin >> arr[i].P >> arr[i].I >> arr[i].B;
        addC++;

        cout << i + 1 << "." << addC << " Enter NMT results: ";
        cin >> arr[i].resultNMT[0] >> arr[i].resultNMT[1] >> arr[i].resultNMT[2];
        addC++;

        cout << i + 1 << "." << addC << " Enter additional score: ";
        cin >> arr[i].additionalScore[0] >> arr[i].additionalScore[1] >> arr[i].additionalScore[2];
        addC++;

        cout << i + 1 << "." << addC << " Enter university name: ";
        cin >> arr[i].universityName;
        addC++;

        cout << i + 1 << "." << addC << " Enter specialization: ";
        cin >> arr[i].specialization;
        addC++;

        arr[i].totalNMTscore = (arr[i].resultNMT[0] * arr[i].additionalScore[0] + arr[i].resultNMT[1] * arr[i].additionalScore[1] + arr[i].resultNMT[2] * arr[i].additionalScore[2]) * 1.04;
        cout << i + 1 << "." << addC << " Total NMT score: " << arr[i].totalNMTscore << endl;
        addC++;

        cout << endl;
    }
}

void fillArr(studentsData *arr, int n, const string &file)
{
    fstream f(file.c_str(), ios::in);
    vector<string> av;
    string a;

    while (getline(f, a))
        if (!(a.empty()))
            av.push_back(a);

    for (int i = 0, j = 0; i < n; i++, j += 11)
    {
        arr[i].P = av.at(j);
        arr[i].I = av.at(j + 1);
        arr[i].B = av.at(j + 2);

        arr[i].resultNMT[0] = stoi(av.at(j + 3));
        arr[i].resultNMT[1] = stoi(av.at(j + 4));
        arr[i].resultNMT[2] = stoi(av.at(j + 5));

        arr[i].additionalScore[0] = stod(av.at(j + 6));
        arr[i].additionalScore[1] = stod(av.at(j + 7));
        arr[i].additionalScore[2] = stod(av.at(j + 8));

        arr[i].universityName = av.at(j + 9);

        arr[i].specialization = av.at(j + 10);

        arr[i].totalNMTscore = (arr[i].resultNMT[0] * arr[i].additionalScore[0] + arr[i].resultNMT[1] * arr[i].additionalScore[1] + arr[i].resultNMT[2] * arr[i].additionalScore[2]) * 1.04;
    }

    showStudents(arr, n);
    return;
}

int countStudents(const string &filename)
{
    fstream f(filename.c_str(), ios::in);
    string a;
    int count = 1;

    while (getline(f, a))
        if (a.empty())
            count++;

    return count;
}

// create a function that will take file name from user
string fileNameInput()
{
    // declare local variables
    bool isExtensionFound = false;
    string input;

    // ask user to input file name
    cout << "Enter the name of the file: ";
    cin >> input;
    cin.ignore();

    // create for loop to look for extension
    for (int i = 0; i < input.length(); i++)
    {
        // dot is an indication of extension
        if (input[i] == '.')
        {
            // if found then change bool isExtensionFound to true
            isExtensionFound = true;
            break; // break out of loop
        }
    }

    // if the result is not found then
    if (!isExtensionFound)
    {
        // create a new string for holding the file extension
        string fileExtension;

        // ask user to enter a file extension
        cout << "Please specify a file extension: ";
        cin >> fileExtension;
        cin.ignore();

        // create a for loop
        for (int i = 0; i < fileExtension.length(); i++)
        {
            // look for a dot in input
            if (fileExtension[i] == '.')
            {
                // if found then add it to the result string
                input += fileExtension;
                break; // break out of loop
            }
            else
            {
                // if not found then add add a dot + input to the result string
                input += "." + fileExtension;
                break; // break out of loop
            }
        }
    }

    // return the result string
    return input;
}

// create a function that will generate random string
string randString(int ch)
{
    // declare max array length
    const int maxArrSize = 25;
    // declare possible characters
    char possibleCharactersArr[maxArrSize] = {'a', 'b', 'c', 'd', 'e', 'f', 'g',
                                              'h', 'i', 'j', 'k', 'l', 'm', 'n',
                                              'o', 'p', 'q', 'r', 's', 't', 'u',
                                              'v', 'w', 'x', 'y'};
    // declare result string
    string result = "";
    // create for loop
    for (int i = 0; i < ch; i++)
        // add random character from an earlier declared set to the string
        result += possibleCharactersArr[rand() % maxArrSize];

    // add file extension to result
    result += ".txt";
    // return result
    return result;
}