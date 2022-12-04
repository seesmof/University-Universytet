#include <bits/stdc++.h>
using namespace std;

int main()
{
    srand(time(NULL));
    cout << endl
         << "/////////////////////////////////////////////////////////////" << endl
         << endl;

    // declare variables for future use
    int n;
    cout << "Enter the number of elements: ";
    cin >> n;
    int arr[n][n];
    int decision;
    char ans;

    // ask user to choose whether they want an array to be generated or entered
    cout << endl
         << "Do you want to enter the array yourself or get a generated one?" << endl;
    cout << "1 to enter | 2 to generate" << endl;
    // create a do while loop
    do
    {
        // ask user to enter decision
        cout << "Enter: ";
        cin >> decision;
        // if 1 entered
        if (decision == 1)
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
        else if (decision == 2)
        {
            // generate array elements in range from 10 to 100
            for (int i = 0; i < n; i++)
                for (int j = 0; j < n; j++)
                    arr[i][j] = 10 + rand() % ((100 + 1) - 10);
            break;
        }
        // if something else was entered
        else
        {
            // output error
            cout << "Error: Unknown input." << endl;
            // ask if they want to enter again
            cout << "Would you like to continue? (Y | N): ";
            cin >> ans;
            cout << endl;
            continue;
        }
    } while (ans == 'Y' || ans == 'y');

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
    cin >> decision;
    // if 1 entered
    if (decision == 1)
    {
        // sort in ascending order
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                sort(arr[j], arr[j] + n);
    }
    // if 2 entered
    else if (decision == 2)
    {
        // sort in descending order
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                sort(arr[j], arr[j] + n);
                reverse(arr[j], arr[j] + n);
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

    cout << endl
         << "/////////////////////////////////////////////////////////////" << endl
         << endl;
    return 0;
}