// include necessary libraries
#include <iostream>
#include <math.h>
using namespace std;

// declare main function
int main(int argc, char **argv)
{
    // output program intro
    cout << endl;
    cout << "****************************** Task A *************************************" << endl
         << endl;

    int n, counter;
    cout << "Enter array size: ";
    cin >> n;
    double *arr = new double[n];

    for (int i = 0; i < n; i++)
    {
        cout << "Enter element " << i + 1 << ": ";
        cin >> arr[i];
    }
    cout << endl;
    cout << "You array is: ";
    for (int i = 0; i < n; i++)
    {
        cout << arr[i] << " ";
    }
    cout << endl
         << endl;
    for (int i = 0; i < n; i++)
    {
        counter = 0;
        for (int j = 0; j < n; j++)
        {
            if (arr[i] == arr[j])
            {
                counter++;
            }
        }
        cout << "Number " << arr[i] << " was entered " << counter << " times" << endl;
    }

    // output project outro
    cout << endl;
    cout << "***************************************************************************" << endl
         << endl;

    // end main function
    return 0;
}
