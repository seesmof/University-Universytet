// include necessary libraries
#include "../lib.h"
using namespace std;

// func main start
int main()
{
    // declare local variables //
    srand(time(NULL));
    char doContinue;
    ll userDecision;
    /////////////////////////////

    // project intro
    cout << "\n";
    do
    {
        ///////////////////////////////////////
        char input;
        cout << "Enter: ";
        cin >> input;
        cout << char(tolower(input));
        cin.ignore();
        ///////////////////////////////////////

        // ask user if they would like to continue execution of program
        cout << GRAY << "\nWould you like to continue program execution? (Y | N): " << UNGRAY;
        cin >> doContinue;
        if (doContinue == 'Y' || doContinue == 'y')
        {
            cout << "\n\n";
            continue;
        }
        else
            break;
    } while (doContinue = 'Y' || doContinue == 'y');

    // stop main function execution
    cout << "\nThanks for using this program\n\n";
    return 0;
}