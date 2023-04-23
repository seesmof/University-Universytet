#include "D:\repos\university\lib.h"
#include "exc.h"

class Exception : public exception
{
public:
    virtual const char *what() const throw()
    {
        return "Unknown exception occurred.";
    }
};

class FileException : public Exception
{
public:
    void checkFile(const std::string &filename)
    {
        std::fstream file(filename);
        if (!file.is_open())
        {
            throw std::runtime_error("File not found or cannot be opened");
        }
    }
};

class Arithmetic_Exception : public Exception
{
public:
    bool divisionByZero(double divisor) const
    {
        return true;
    }
};

class Memory_Exception : public Exception
{
public:
    bool allocationError() const
    {
        return true;
    }
};

/*
int main()
{
    IO_Exception io;
    if (io.fileNotFound("file.txt"))
    {
        cout << "File not found.\n";
    }

    Arithmetic_Exception arith;
    if (arith.divisionByZero(0))
    {
        cout << "Division by zero.\n";
    }

    Memory_Exception mem;
    if (mem.allocationError())
    {
        cout << "Error during dynamic memory allocation.\n";
    }

    return 0;
}
*/