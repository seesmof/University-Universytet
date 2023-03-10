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
        vector<unique_ptr<Stud>> studentVector;
        // for manipulating program flow
        char doReturnToMenu;

        do
        {
            outputMenu(studentVector);

            // ask user if they would like to return to menu
            cout << "Would you like to return to menu? (Y | N): ";
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