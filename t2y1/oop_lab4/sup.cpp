#include <bits/stdc++.h>
#include "sup.h"
#include "../../lib.h"
using namespace std;

/*
Варіант 5. Створити динамічний клас для роботи з рядками (послідовностями символів). Максимальна довжина послідовності – 65535, код завершення послідовності – нуль. Здійснити перевантаження символів операцій:
"="	– динамічне присвоєння,
" << " , " >> " – консольне введення-виведення значень;
" << " , " >> "  - введення із файлу і виведення у файл з символами таким чином:
f << A або A >> f – виведення (запис) значення A в файл f,
f >> A або A << f – введення (читання) значення A з файлу f.
*/

class DynamicString
{
public:
    DynamicString();                                                      // default constructor
    DynamicString(const char *str);                                       // constructor with parameter
    ~DynamicString();                                                     // destructor
    DynamicString &operator=(const char *str);                            // assignment operator
    friend ostream &operator<<(ostream &out, const DynamicString &str);   // console output operator
    friend istream &operator>>(istream &in, DynamicString &str);          // console input operator
    friend ofstream &operator<<(ofstream &out, const DynamicString &str); // file output operator
    friend ifstream &operator>>(ifstream &in, DynamicString &str);        // file input operator
private:
    char *m_data;  // pointer to the string data
    size_t m_size; // size of the string data
};

DynamicString::DynamicString() : m_data(nullptr), m_size(0) {}

DynamicString::DynamicString(const char *str) : m_data(nullptr), m_size(0)
{
    if (str)
    {
        m_size = strlen(str) + 1;
        m_data = new char[m_size];
        strcpy_s(m_data, m_size, str);
    }
}

DynamicString::~DynamicString()
{
    delete[] m_data;
}

DynamicString &DynamicString::operator=(const char *str)
{
    if (str)
    {
        size_t size = strlen(str) + 1;
        char *data = new char[size];
        strcpy_s(data, size, str);
        delete[] m_data;
        m_data = data;
        m_size = size;
    }
    return *this;
}

ostream &operator<<(ostream &out, const DynamicString &str)
{
    out << str.m_data;
    return out;
}

istream &operator>>(istream &in, DynamicString &str)
{
    char buffer[65536];
    in.getline(buffer, 65536);
    str = buffer;
    return in;
}

ofstream &operator<<(ofstream &out, const DynamicString &str)
{
    out << str.m_data;
    return out;
}

ifstream &operator>>(ifstream &in, DynamicString &str)
{
    char buffer[65536];
    in.getline(buffer, 65536);
    str = buffer;
    return in;
}
