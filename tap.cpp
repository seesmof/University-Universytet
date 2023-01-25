#include <bits/stdc++.h>
using namespace std;

int main()
{
    time_t now = time(0);
    tm *ltm = localtime(&now);

    int day = ltm->tm_mday;
    int month = 1 + ltm->tm_mon;
    int year = 1900 + ltm->tm_year;
    int hour = ltm->tm_hour;
    int min = ltm->tm_min;

    stringstream recievedDateHolder;
    recievedDateHolder << (day < 10 ? "0" : "") << day << "."
                       << (month < 10 ? "0" : "") << month << "."
                       << year << " "
                       << (hour < 10 ? "0" : "") << hour << ":"
                       << (min < 10 ? "0" : "") << min;
    string recievedDate = recievedDateHolder.str();

    cout << recievedDate << endl;

    return 0;
}