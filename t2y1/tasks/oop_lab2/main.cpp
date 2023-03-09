// include necessary libraries
#include "../../../lib.h"
#include "sup.h"
using namespace std;

// Варіант 5. Створити динамічний клас Route на основі двозв’язного списку, де кожний елемент типа stop (зупинка). Клас повинен містити наступні операції:
// add_stop() – додавання зупинки;
// len_route() – розрахунок довжини маршруту;
// time_route() – розрахувати час руху.

class Stop
{
public:
    string name;
    double distance;
    Stop *next;
    Stop *prev;

    Stop(string name, double distance)
    {
        this->name = name;
        this->distance = distance;
        this->next = nullptr;
        this->prev = nullptr;
    }
};

class Route
{
public:
    Stop *head;
    Stop *tail;

    Route()
    {
        this->head = nullptr;
        this->tail = nullptr;
    }

    void add_stop(string name, double distance)
    {
        Stop *stop = new Stop(name, distance);
        if (head == nullptr)
        {
            head = stop;
            tail = stop;
        }
        else
        {
            tail->next = stop;
            stop->prev = tail;
            tail = stop;
        }
    }

    int len_route()
    {
        Stop *current = head;
        int count = 0;
        while (current != nullptr)
        {
            count++;
            current = current->next;
        }
        return count;
    }

    double time_route()
    {
        Stop *current = head;
        double total_time = 0.0;
        while (current != nullptr)
        {
            total_time += current->distance;
            current = current->next;
        }
        return total_time;
    }
};

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
        vector<unique_ptr<Delta>> deltaObjectsVector;
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