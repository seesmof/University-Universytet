// include necessary libraries
#include <bits/stdc++.h>
using namespace std;

// function prototypes //

/////////////////////////

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
         << "\nWelcome! This program will sort a 2D matrix\n"
         << "\n/////////////////////////////////////////////////////////////\n\n";
    do
    {
        //////////////////////////////////////////////////////////////////////////////////
        // declare variables for future use
        int n;
        cout << "Enter the number of elements: ";
        cin >> n;
        vector<vector<int>> arr(n, vector<int>(n));

        // ask user to choose whether they want an array to be generated or entered
        cout << endl
             << "Do you want to enter the array yourself or get a generated one?" << endl;
        cout << "1 to enter | 2 to generate" << endl;
        // create a do while loop
        do
        {
            // ask user to enter decision
            cout << "Enter: ";
            cin >> userDecision;
            // if 1 entered
            if (userDecision == 1)
            {
                // prompt user to enter each array element
                for (int i = 0; i < n; i++)
                {
                    for (int j = 0; j < n; j++)
                    {
                        cout << "Enter an element: ";
                        cin >> arr[i][j];
                    }
                }
                break;
            }
            // if 2 entered
            else if (userDecision == 2)
            {
                // generate array elements in range from 10 to 100
                for (int i = 0; i < n; i++)
                    for (int j = 0; j < n; j++)
                        arr[i][j] = rand() % 10;
                break;
            }
            // if something else was entered
            else
            {
                // output error
                cout << "Error: Unknown input." << endl;
                // ask if they want to enter again
                cout << "Would you like to continue? (Y | N): ";
                cin >> doContinue;
                cout << endl;
                continue;
            }
        } while (doContinue == 'Y' || doContinue == 'y');

        // output array to user
        cout << endl
             << "Your array is: " << endl;
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                if (j == 0)
                    cout << arr[i][j];
                else
                    cout << setw(4) << arr[i][j];
            }
            cout << endl;
        }

        // ask user in what way they want an array to be sorted
        cout << endl
             << "In what order would you like to sort it?" << endl;
        cout << "1 for ascending | 2 for descending" << endl;
        cout << "Enter: ";
        cin >> userDecision;
        // if 1 entered
        if (userDecision == 1)
        {
            // sort in ascending order
            for (int i = 0; i < n; i++)
                for (int j = 0; j < n; j++)
                    sort(arr[j].begin(), arr[j].end());
        }
        // if 2 entered
        else if (userDecision == 2)
        {
            // sort in descending order
            for (int i = 0; i < n; i++)
            {
                for (int j = 0; j < n; j++)
                {
                    sort(arr[j].begin(), arr[j].end());
                    reverse(arr[j].begin(), arr[j].end());
                }
            }
        }

        // output final array
        cout << endl
             << "Your sorted array is: " << endl;
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                if (j == 0)
                    cout << arr[i][j];
                else
                    cout << setw(4) << arr[i][j];
            }
            cout << endl;
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