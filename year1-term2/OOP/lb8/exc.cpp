#include "D:\repos\university\lib.h"
#include "exc.h"

/*
Створити  базовий  клас  Exception,  та  відповідні  класи-спадкоємці, що дозволяють обробляти наступні виняткові ситуації:
    а)  помилки  при  роботі  з  потоками  введення/виведення, зокрема при роботі з  файлами;
    б)  помилки арифметичних операцій (ділення на 0);
    в)  помилки  виділення  динамічної  пам’яті  при перевантаженні операторів new  та delete.
*/

class Exception
{
public:
    virtual const char *what() const throw()
    {
        bad("An exception has occurred");
    }
};

class IOException : public Exception
{
public:
    const char *what() const throw() override
    {
        bad("I/O stream error");
    }
};

class ArithmeticException : public Exception
{
public:
    const char *what() const throw() override
    {
        bad("Arithmetic error: division by zero");
    }
};

class MemoryException : public Exception
{
public:
    const char *what() const throw() override
    {
        bad("Memory allocation error");
    }
};