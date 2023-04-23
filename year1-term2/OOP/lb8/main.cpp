// include necessary libraries
#include "D:\repos\university\lib.h"
#include "sup.h"
#include "exc.h"
using namespace std;

// Для завдання з лабораторної роботи #5 виконати обробку виняткових ситуацій з використанням класу Exception.

// func main start
int main()
{
    // declare local variables //
    srand(time(NULL));
    char doContinue;
    /////////////////////////////

    IO_Exception io;
    if (io.fileNotFound("file.txt"))
    {
        cout << "File not found.\n";
    }

    Arithmetic_Exception arith;
    if (arith.divisionByZero(0))
    {
        cout << "Division by zero.\n";
    }

    Memory_Exception mem;
    if (mem.allocationError())
    {
        cout << "Error during dynamic memory allocation.\n";
    }

    // project intro
    cout << "\n";
    do
    {
        ///////////////////////////////////////

        // for storing class object pointers
        vector<DynamicString> container;
        // for manipulating program flow
        char doReturnToMenu;

        do
        {
            // output menu to user
            outputMenu(container);

            // ask user if they would like to return to menu
            cout << "\nWould you like to return to menu? (Y | N): ";
            cin >> doReturnToMenu;
            // if so, continue loop execution
            if (doReturnToMenu == 'Y' || doReturnToMenu == 'y')
            {
                cout << endl
                     << endl;
                continue;
            }
            // if not, break out of loop
            else
                break;

        } while (doReturnToMenu == 'y' || doReturnToMenu == 'Y');
        // execute while user chooses to return to menu

        ///////////////////////////////////////

        // ask user if they would like to continue execution of program
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

    // stop main function execution
    cout << "\nThanks for using this program\n\n";
    return 0;
}