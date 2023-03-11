// include necessary libraries
#include "../../../lib.h"
#include "sup.h"
using namespace std;

// *Варіант* 5.Створити базовий клас Людина, відповідно до варіанту 4.
// Створити похідний клас Інженер, що містить додаткові дані: рік закінчення, ВУЗ, спеціальність, тип диплому, тип навчання, перекваліфікація (динамічний масив), місце роботи, заробітня платня.
// Клас повинен містити наступні методи: ініціалізації інформації, розрахунок заробітної платні, розрахунок щорічного доходу, додавання інформацій щодо перекваліфікації.
// *Варіант* 4.Створити базовий клас Людина. Кожний об’єкт класу повинен містити наступні дані: ПІБ, рік народження, стать.
// Клас повинен виконувати наступні дії: ініціалізація інформації, введення-виведення інформації.
// Створити похідний клас Студент, що має додаткові дані: рік вступу, № залікової книжки, кількість дисциплін що вивчається, дисципліни (динамічний масив), середній бал.
// Клас повинен виконувати наступні функції: ініціалізація інформації, додавання дисциплін, розрахунок середнього балу, виводити загальну інформацію про студента.

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
        Route routeVector;
        // for manipulating program flow
        char doReturnToMenu;

        do
        {
            outputMenu(routeVector);

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