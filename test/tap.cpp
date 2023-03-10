#include "../lib.h"
using namespace std;

int main()
{
    // create a time struct to get current year
    time_t t = time(NULL);
    struct tm *tm = localtime(&t);
    // get student's birth year and current year
    ll currentYear = tm->tm_year;
    cout << currentYear << endl;

    return 0;
}
