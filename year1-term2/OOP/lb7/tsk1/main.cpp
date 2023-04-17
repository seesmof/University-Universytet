// include necessary libraries
#include "D:\repos\university\lib.h"
#include "sup.h"

// Створити клас Delta таким чином, щоб кожний об’єкт вміщував свій персональний номер (дескриптор об’єкта) та функцію, яка повертає його значення. Дескриптор об’єкта – унікальне для об’єктів даного типу ціле число.
// Виконати завдання з лабораторної роботи №1, де тип елементу заданої структури даних довільний. Використати шаблонні функції.

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

        char doReturnToMenu;
        do
        {
            // output menu to user and prompt them to choose an option
            cout << BOLD << "Choose an option from menu\n"
                 << UNBOLD;
            cout << "1. Add objects\n";
            cout << "2. Delete objects\n";
            cout << "3. Print objects\n";
            cout << "4. Exit\n";
            cout << "\nEnter: ";
            userDecision = getNum();
            cout << endl;

            // if user chose to add objects
            if (userDecision == 1)
            {
                vector<unique_ptr<Delta<dataType>>> deltaObjectsVector;
                // add objects
                createObjects(deltaObjectsVector);
                // print them to console
                printObjects(deltaObjectsVector);
            }
            // if user chose to delete objects
            else if (userDecision == 2)
            {
                // delete them
                deleteObjects(deltaObjectsVector);
                // print them to console
                printObjects(deltaObjectsVector);
            }
            // if user chose to print objects
            else if (userDecision == 3)
                // print objects to console
                printObjects(deltaObjectsVector);

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