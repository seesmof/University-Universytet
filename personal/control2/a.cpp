// include necessary libraries
#include <bits/stdc++.h>
using namespace std;

// function prototypes //
string getFileName();
void fillVector(int, int, string, vector<vector<int>> &);
void fillVector(int, int, vector<vector<int>> &);
void outputVector(int, int, vector<vector<int>> &);
ostream &BOLD(ostream &);
ostream &UNBOLD(ostream &);
ostream &RED(ostream &);
ostream &UNRED(ostream &);
/////////////////////////

void getResult(int n, int m, vector<vector<int>> &a, int x, int y)
{
    const int startingPointN = 0, startingPointM = m - 1;
    x -= 1;
    y -= 1;
    int currentPosN = startingPointN, currentPosM = startingPointM;

    do
    {
        bool moveLeft = false;
        int leftI = currentPosN, leftJ = currentPosM - 1;
        int downI = currentPosN + 1, downJ = currentPosM;
        int left, down;

        cout << "\nCurrent position is displayed in bold, legal moves are displayed in red\n";
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < m; j++)
            {
                if (i == currentPosN && j == currentPosM)
                    cout << BOLD << a[i][j] << UNBOLD << " ";
                else if (i == leftI && j == leftJ)
                {
                    cout << RED << a[i][j] << UNRED << " ";
                    left = a[i][j];
                }
                else if (i == downI && j == downJ)
                {
                    cout << RED << a[i][j] << UNRED << " ";
                    down = a[i][j];
                }
                else
                    cout << a[i][j] << " ";
            }
            cout << endl;
        }
        if (left <= down)
            moveLeft = true;
        else
            moveLeft = false;

        if (!moveLeft)
        {
            cout << "Your next move should be down\n";
        }
        else
        {
            cout << "Your next move should be left\n";
        }

        char move;
        cout << "\nYour move is (L / D): ";
        cin >> move;

        if (move == 'l' || move == 'L')
        {
            currentPosM -= 1;
            continue;
        }
        else
        {
            currentPosN += 1;
            continue;
        }
    } while (currentPosN != y && currentPosM != x);
}

// func main start
int main()
{
    // declare local variables //
    srand(time(NULL));
    char doContinue;
    int userDecision;
    /////////////////////////////

    // project intro
    cout << "\n/////////////////////////////////////////////////////////////\n"
         << "\nWelcome! This is task A\n"
         << "\n/////////////////////////////////////////////////////////////\n\n";
    do
    {
        //////////////////////////////////////////////////////////////////////////////////
        cout << BOLD << "Would you like to enter field data from file or from command line?\n"
             << UNBOLD;
        cout << "1. Enter from file\n";
        cout << "2. Enter from command line\n";
        cout << "Input: ";
        cin >> userDecision;
        cout << endl;

        string inFileName;
        int rows, cols;
        vector<vector<int>> matrixVector;
        if (userDecision == 1)
        {
            inFileName = getFileName();

            cout << "\nEnter number of rows and columns in matrix (R C): ";
            cin >> rows >> cols;

            fillVector(rows, cols, inFileName, matrixVector);
            cout << "\nYour array is: \n";
            outputVector(rows, cols, matrixVector);
        }
        else
        {
            cout << "Enter number of rows and columns in matrix (R C): ";
            cin >> rows >> cols;

            fillVector(rows, cols, matrixVector);
            cout << "\nYour array is: \n";
            outputVector(rows, cols, matrixVector);
        }

        cout << BOLD << "\nWould you like to play the game here or just get the answer?\n"
             << UNBOLD;
        cout << "1. Play live\n";
        cout << "2. Get the answer\n";
        cout << "Input: ";
        cin >> userDecision;

        int resX, resY;
        cout << "\nEnter finish point coordinates (X Y): ";
        cin >> resX >> resY;

        getResult(rows, cols, matrixVector, resX, resY);
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

// for outputting 2D matrix
void outputVector(int n, int m, vector<vector<int>> &a)
{
    // create for loop for iterating over an array
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            // output each element
            cout << a[i][j] << " ";
        }
        cout << endl;
    }
    // end function
    return;
}

// for entering matrix by hand
void fillVector(int n, int m, vector<vector<int>> &a)
{
    int userDecision;
    cout << BOLD << "\nWould you like to enter or generate a matrix?\n"
         << UNBOLD;
    cout << "1. Enter matrix by yourself\n";
    cout << "2. Generate random matrix\n";
    cout << "Input: ";
    cin >> userDecision;
    cout << endl;

    int element; // for storing current element

    // create loop for iterating over the matrix
    for (int i = 0; i < n; i++)
    {
        // declare vector for storing row elements
        vector<int> row;
        for (int j = 0; j < m; j++)
        {
            if (userDecision == 1)
            {
                // ask user to enter an element
                cout << "Enter element: ";
                cin >> element;
            }
            else
            {
                element = rand() % 10;
            }
            // push back element intro row array
            row.push_back(element);
        }
        // add row array to general matrix
        a.push_back(row);
    }
    // end function
    return;
}

// for reading matrix from file
void fillVector(int n, int m, string file, vector<vector<int>> &a)
{
    int element;                      // for storing current element
    fstream f(file.c_str(), ios::in); // for reading file

    // if file is not opened
    if (!f.is_open())
    {
        // output error message
        cout << RED << "\nERROR: Could not open file " << file << endl
             << UNRED;
        // stop function execution
        return;
    }

    // create loop for iterating over the matrix
    for (int i = 0; i < n; i++)
    {
        // declare vector for storing row elements
        vector<int> row;
        for (int j = 0; j < m; j++)
        {
            // read element from file
            f >> element;
            // push back element intro row array
            row.push_back(element);
        }
        // add row array to general matrix
        a.push_back(row);
    }
    // close file and end function
    f.close();
    return;
}

// getting file name from user
string getFileName()
{
    string fileName = "";         // for storing file name
    bool isExtensionFound = true; // for getting file extension
    bool doesFileExist = false;   // for knowing if file exists

    do
    {
        // do while no extension is found
        do
        {
            // ask to enter file name
            cout << "Enter file name: ";
            cin >> fileName;

            // if extension is not found
            if (fileName.find(".") == string::npos)
            {
                // output error message
                isExtensionFound = false;
                cout << RED << "\nERROR: File extension not found. Try again...\n\n"
                     << UNRED;
                // continue loop execution
                continue;
            }
            else
                break;
        } while (isExtensionFound == false);

        // check if file exists
        fstream file(fileName.c_str());
        // if not => output error
        if (!file.good())
        {
            cout << RED << "\nERROR: Could not open file " << fileName << "\n\n"
                 << UNRED;
            doesFileExist = false;
            continue;
        }
        // if yes => end loop
        else
            break;
    } while (doesFileExist == false);

    // return file name
    return fileName;
}

// making output text bold
ostream &BOLD(ostream &os)
{
    return os << "\e[1m";
}

// making output text normal
ostream &UNBOLD(ostream &os)
{
    return os << "\e[0m";
}

// to make text red
ostream &RED(ostream &os)
{
    return os << "\033[1;31m";
}

// to change text back to normal
ostream &UNRED(ostream &os)
{
    return os << "\033[0m";
}