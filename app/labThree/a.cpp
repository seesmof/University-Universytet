#include <iostream>
using namespace std;

int main(int argc, char **argv)
{
    int holder[10];
    for (int i = 0; i < 10; i++)
    {
        cout << "Enter some number: ";
        cin >> holder[i];
    }
    cout << "Our array consists of ";
    for (int i = 0; i < 10; i++)
    {
        cout << holder[i] << " ";
    }
    return 0;
}