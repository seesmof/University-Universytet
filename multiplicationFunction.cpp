#include <iostream>
using namespace std;

// Declare function that multiplies two numbers
int func(int a, int b)
{
    int result = a * b;
    return result;
}

int main(int argc, char **argv)
{
    int result, numberA, numberB;

    // Ask for first number from user
    cout << "First number: " << endl;
    cin >> numberA;

    // Ask for second number from user
    cout << "Second number: " << endl;
    cin >> numberB;

    // Multiply them and return result
    result = func(numberA, numberB);
    cout << "Result is: " << result << endl;

    return 0;
}