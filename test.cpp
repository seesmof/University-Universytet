#include <iostream>
#include <math.h>
#include <string.h>

using namespace std;

void REG()
{
    string lname, fname, city;
    int bday, bmonth, byear;

    cout << "Welcome to SkylinesBank! Thank you for choosing us!" << endl
         << endl;

    cout << "Please enter your first name: " << endl;
    cin >> fname;
    cout << "Please enter your last name: " << endl;
    cin >> lname;
}

void LOGIN()
{
    string login;
    int password;

    cout << "Sike" << endl;
}

int main()
{
    int input;

    cout << "Welcome to SkilinesBank! Thank you for choosing us. Please follow the instructions to create your account." << endl;
    cout << "If you already have an account, you can login by typing 1 below. Otherwise, type 0" << endl;
    cin >> input;
    if (input == 1)
    {
        LOGIN();
    }
    else
    {
        REG();
    }
}