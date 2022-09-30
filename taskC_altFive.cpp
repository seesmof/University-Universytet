#include <iostream>
#include <math.h>

using namespace std;

int main(int argc, char **argv)
{
    int exp, nad;
    double wage, result;

    cout << "Enter the years of experience: " << endl;
    cin >> exp;
    cout << "Enter the wage you are getting: " << endl;
    cin >> wage;

    if (exp >= 5 && exp <= 10)
    {
        nad = wage * 0.01;
        result = wage + nad;
        cout << "Your final salary is " << result << endl;
    }
    else if (exp >= 10)
    {
        nad = wage * 0.05;
        result = wage + nad;
        cout << "Your final salary is " << result << endl;
    }
    else
    {
        cout << "Your final salary will stay the same" << endl;
    }

    return 0;
}

// 1.3.2.23 г)