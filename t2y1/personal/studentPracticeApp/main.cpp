// include necessary libraries
#include "../../../lib.h"
#include "sup.h"
using namespace std;

// Розробити клас Stud, Який містить інформацію про ім'я студента, рік його народження. Передбачити: можливість автоматичної нумерації створених оь'єктів класу, ініціалізацію об'єктів пустими параметрами та параметрами визначеними зазделагідь, можливість запису та зчитування полів класу із-зовні, встановлення полів об'єкту із запитом до користувача та через передані дані, виведення всієї інформації на екран, зміну параметрів об'єкта, дружню функцію для підрахунку віку студента.

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

        // for storing class object pointers
        vector<unique_ptr<Stud>> deltaObjectsVector;
        // for manipulating program flow
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
            cin >> userDecision;

            // check if input is not an integer
            if (cin.fail())
            {
                // output error
                cout << RED << "\nERROR: Enter an integer...\n\n"
                     << UNRED;
                // clear buffer
                cin.clear();
                cin.ignore();
                // break out of loop
                break;
            }

            // if user chose to add objects
            if (userDecision == 1)
            {
            }
            // if user chose to delete objects
            else if (userDecision == 2)
            {
            }
            // if user chose to print objects
            else if (userDecision == 3)
            {
            }

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