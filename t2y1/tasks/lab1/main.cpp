// include necessary libraries
#include "../../../lib.h"
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
    cout << "\n";
    do
    {
        //////////////////////////////////////////////////////////////////////////////////
        cout << "Testing\n";
        //////////////////////////////////////////////////////////////////////////////////
        cout << "\nWould you like to continue program execution? (Y | N): ";
        cin >> doContinue;
        if (doContinue == 'Y' || doContinue == 'y')
        {
            cout << "\n\n";
            continue;
        }
        else
            break;
    } while (doContinue = 'Y' || doContinue == 'y');

    // End main function
    cout << "\nThanks for using this program\n\n";
    return 0;
}