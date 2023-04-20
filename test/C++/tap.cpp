#include <iostream>
#include <cstdlib> // For rand() and srand()
#include <ctime>   // For time()
#include <string>

using namespace std;

float MyFunction(int number)
{
    float result = 1;
    for (int a = 0; a < number; a += 5)
    {
        result = result * (a < 10 ? 2 : 1.5);
    }
    return result;
}

int main()
{
    cout << MyFunction(17);
    return 0;
}
