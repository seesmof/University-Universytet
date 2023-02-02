// include necessary libraries
#include "../../../lib.h"
using namespace std;

ll userDecision;
struct User
{
    string userName;
    string password;
};

// function prototypes //
void mainMenu();
void authMenu(vector<User> &);
void paymentsMenu();
void getUsers(vector<User> &);
/////////////////////////

// func main start
int main()
{
    // declare local variables //
    srand(time(NULL));
    char doContinue;
    /////////////////////////////

    // project intro
    cout << "\n/////////////////////////////////////////////////////////////\n"
         << "\nWelcome to UnifyBank - Your Financial Ally for Every Journey.\n"
         << "\n/////////////////////////////////////////////////////////////\n\n";
    do
    {
        //////////////////////////////////////////////////////////////////////////////////

        vector<User> userVector;
        getUsers(userVector);
        cout << endl;

        authMenu(userVector);
        cout << endl;

        do
        {
            mainMenu();
            cout << endl;

            cout << BOLD << "Would you like to go back to main menu? (Y | N): " << UNBOLD;
            cin >> doContinue;
            if (doContinue == 'y' || doContinue == 'Y')
                continue;
            else
                break;

        } while (doContinue == 'Y' || doContinue == 'y');

        //////////////////////////////////////////////////////////////////////////////////
        cout << "\n/////////////////////////////////////////////////////////////\n"
             << "\nWould you like to continue program execution? (Y | N): ";
        cin >> doContinue;
        if (doContinue == 'Y' || doContinue == 'y')
        {
            cout << "\n/////////////////////////////////////////////////////////////\n\n";
            continue;
        }
        else
            break;
    } while (doContinue = 'Y' || doContinue == 'y');

    // func main end
    cout << "\nThanks for using this program\n"
         << "\n/////////////////////////////////////////////////////////////\n\n";
    return 0;
}

void getUsers(vector<User> &userVector)
{
    string fileName = "users.txt";
    fstream file(fileName.c_str(), ios::in);
    vector<string> lines;
    string line;

    if (!file.is_open())
    {
        cout << RED << "\nERROR: Couldn't open users data file " << fileName << endl
             << UNRED;
        return;
    }

    ll userCount = 1;
    while (getline(file, line))
    {
        if (line.empty())
        {
            userCount++;
            continue;
        }
        else
            lines.pb(line);
    }

    for (ll i = 0, j = 0; i < userCount; i++, j += 2)
    {
        userVector.pb(User());
        userVector[i].userName = lines[j];
        userVector[i].password = lines[j + 1];
    }
}

void authMenu(vector<User> &userVector)
{
    cout << BOLD << "How would you like to access our banking services?\n"
         << UNBOLD;
    cout << "1. Login\n";
    cout << "2. Sign up\n";
    cout << "3. Incognito\n";
    cout << "4. Exit\n";
    cout << GRAY << "\nPlease note that incognito mode has some limitations\n\n"
         << UNGRAY;
    cout << "Make a choice: ";
    cin >> userDecision;
    cout << endl;

    if (userDecision == 1)
    {
        string userName, password;
        cout << "Enter your username: ";
        cin >> userName;
        ll check = 0;
        for (ll i = 0; i < userVector.size(); i++)
        {
            if (userVector[i].userName == userName)
            {
                check++;
                break;
            }
        }
        if (check == 0)
        {
            char doContinue;
            cout << RED << "\nERROR: Could not find an account with username \"" << userName << "\"\n"
                 << UNRED;
            cout << "\nWould you like to sign up? (Y | N) ";
            cin >> doContinue;
        }
    }
    else if (userDecision == 2)
    {
    }
    else if (userDecision == 3)
    {
    }
    else
        return;
}

void paymentsMenu()
{
    cout << BOLD << "What action would you like to perform?\n"
         << UNBOLD;
    cout << "1. Deposit money\n";
    cout << "2. Withdraw money\n";
}

void mainMenu()
{
    cout << BOLD << "What section would you like to go to?\n"
         << UNBOLD;
    cout << "1. Payments\n";
    cout << "2. Investments\n";
    cout << "3. Loans\n";
    cout << "4. Help\n";
    cout << "5. Exit\n";
    cout << "Enter a number of section: ";
    cin >> userDecision;

    // for getting into payments section
    if (userDecision == 1)
    {
    }
    // for getting into investments section
    else if (userDecision == 2)
    {
    }
    // for getting into loans section
    else if (userDecision == 3)
    {
    }
    // for getting into help section
    else if (userDecision == 4)
    {
    }
    else
        return;
}