// include necessary libraries
#include <iostream>
#include <math.h>
using namespace std;

// declare main function
int main(int argc, char **argv)
{
    // output program intro
    cout << endl;
    cout << "****************************** Task B *************************************" << endl
         << endl;

    int n, m;
    cout << "Enter matrix size (n * m): ";
    cin >> n >> m;
    int arr[n][m];
    srand(time(NULL));

    cout << endl;
    cout << "Your matrix is: " << endl;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            arr[i][j] = rand() % 10;
            cout << arr[i][j] << " ";
        }
        cout << endl;
    }
    cout << endl;

    int power;
    cout << "Enter power (n): ";
    cin >> power;

    cout << endl;
    cout << "Your final matrix is: " << endl;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            cout << pow(arr[i][j], power) << " ";
        }
        cout << endl;
    }

    // output project outro
    cout << endl;
    cout << "***************************************************************************" << endl
         << endl;

    // end main function
    return 0;
}
