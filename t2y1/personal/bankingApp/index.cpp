// include necessary libraries
#include "../../../lib.h"
using namespace std;

ll userDecision, INDEX;
string USER_NAME, PIN;
bool isLogedIn = false;
string userFile = "users.txt";
string balanceFile = "balance.txt";

struct User
{
    string userName;
    string password;
    ll balance = 0;
};

// function prototypes //
void mainMenu();
void authMenu(vector<User> &);
void paymentsMenu();
void getUsers(vector<User> &);
void login(vector<User> &);
void signUp(vector<User> &);
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

        if (isLogedIn == false)
            break;

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
    fstream file(userFile.c_str(), ios::in);
    vector<string> lines;
    string line;

    if (!file.is_open())
    {
        cout << RED << "\nERROR: Couldn't open users data file " << userFile << endl
             << UNRED;
        return;
    }

    ll userCount = 0;
    while (getline(file, line))
    {
        if (line.empty())
            userCount++;
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
    cout << "3. Exit\n";
    cout << "Make a choice: ";
    cin >> userDecision;
    cout << endl;

    if (userDecision == 1)
    {
        login(userVector);
    }
    else if (userDecision == 2)
    {
        signUp(userVector);
    }

    return;
}

void login(vector<User> &userVector)
{
    string userName, password;
    cout << "Enter your username: ";
    cin >> userName;

    ll check = 0;
    ll index;
    for (ll i = 0; i < userVector.size(); i++)
    {
        if (userVector[i].userName == userName)
        {
            check++;
            index = i;
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
        if (doContinue == 'y' || doContinue == 'Y')
        {
            signUp(userVector);
            return;
        }
        else
            return;
    }

    bool isPassCorrect = false;
    ll triesCount = 0;
    do
    {
        triesCount++;
        if (triesCount > 3)
        {
            cout << RED << "\nERROR: Too many tries. Try again later...\n"
                 << UNRED;
            return;
        }

        cout << "Enter your password: ";
        cin >> password;
        cout << endl;

        if (password != userVector[index].password)
        {
            cout << RED << "ERROR: Password \"" << password << "\" does not match your password. Please try again...\n\n"
                 << UNRED;
            continue;
        }
        else
        {
            isPassCorrect = true;
            break;
        }

    } while (isPassCorrect == false);

    USER_NAME = userName;
    PIN = password;
    INDEX = index;
    isLogedIn = true;
    cout << GREEN << "Welcome back, " << USER_NAME << endl
         << UNGREEN;
    cout << YELLOW << "Your current balance is $" << userVector[INDEX].balance << endl
         << UNYELLOW;
    return;
}

void signUp(vector<User> &userVector)
{
    cout << BOLD << "Thank you for choosing UnifyBank! We are glad to have you here\n"
         << UNBOLD;
    cout << "Let's register your account, which will not take more than 5 minutes and is absolutely free\n\n";
    string userName, password;
    cout << "Enter your username: ";
    cin >> userName;

    ll seenIndex = 0;
    for (ll i = 0; i < userVector.size(); i++)
    {
        if (userVector[i].userName == userName)
        {
            seenIndex++;
            break;
        }
    }

    if (seenIndex > 0)
    {
        char doContinue;
        cout << RED << "\nUser with such name already exists. Would you like to log in? (Y | N) " << UNRED;
        cin >> doContinue;
        if (doContinue == 'Y' || doContinue == 'y')
        {
            login(userVector);
            return;
        }
    }

    char doContinue;
    cout << BOLD << "Would you like to generate a password? (Y | N) " << UNBOLD;
    cin >> doContinue;
    if (doContinue == 'y' || doContinue == 'Y')
    {
        password = generateRandomPassword(4);
    }
    else
    {
        cout << "Enter your password: ";
        cin >> password;
    }

    PIN = password;
    USER_NAME = userName;

    User user;
    user.userName = userName;
    user.password = password;
    userVector.pb(user);
    isLogedIn = true;
    INDEX = userVector.size() - 1;

    fstream f(userFile.c_str(), ios::app | ios::out);
    if (!f.is_open())
    {
        cout << RED << "\nERROR: Couldn't open user file " << userFile << "\n"
             << UNRED;
        return;
    }
    f << endl;
    f << USER_NAME << endl;
    f << PIN << endl;

    cout << GREEN << "\nWelcome, " << USER_NAME << endl
         << UNGREEN;
    cout << YELLOW << "Your current balance is $" << userVector[INDEX].balance << endl
         << UNYELLOW;

    f.close();
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
        paymentsMenu();
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