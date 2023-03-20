#include <iostream>
#include <iomanip>
using namespace std;

ostream &outsetup(ostream &os)
{
    os.precision(2);
    os << fixed;        // sets float formatting to fixed
    os << showpoint;    // shows trailing zeroes
    os << setfill('-'); // sets fill character to '-'
    os << setw(10);     // sets width to 10 characters
    return os;
}

istream &insetup(istream &is)
{
    is >> noskipws; // disables skipping whitespace
    is.tie(&cout);  // ties input stream to output stream
    return is;
}

void myFunction()
{
    cout << outsetup << "This is some text" << endl;
    double num;
    cout << insetup << "Enter a number: ";
    cin >> num;
    cout << "You entered: " << num << endl;
}

int main()
{
    myFunction();
    return 0;
}
