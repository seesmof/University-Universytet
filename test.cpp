#include <iostream>
using namespace std;

int main(int argc, char **argv)
{
    int a = 200, b = 300;
    double result;
    for (int i = a; i <= b; i++)
    {
        if (i % 3 == 0)
        {
            cout << i << " is divideable by 3" << endl;
        }
    }
    return 0;
}