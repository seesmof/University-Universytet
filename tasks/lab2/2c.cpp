#include <iostream>

using namespace std;

int main(int argc, char **argv)
{
    int pos, neg, in;
    cout << "Enter 0 to stop execution" << endl;
    do
    {
        cout << "Enter a number: ";
        cin >> in;
        if (in < 0)
        {
            neg++;
        }
        else
        {
            pos++;
        }
    } while (in != 0);
    if (neg > pos)
    {
        cout << "More negatives than positive" << endl;
    }
    else if (neg < pos)
    {
        cout << "More positive than negative" << endl;
    }
    else
    {
        cout << "Equal negative and positive" << endl;
    }
    return 0;
}