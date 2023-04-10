#include "../lib.h"

class base
{

    int a;

    float b;
};

class derived : public base
{

    int b1;

    float b[6];
};

int main()
{
    cout << "Hello world!" << endl;
    for (int i = 0; i < 10; i++)
        cout << i << endl;

    return 0;
}
