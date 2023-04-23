#include "D:\repos\university\lib.h"
#include "exc.h"

class Exception : public std::exception
{
public:
    virtual const char *what() const throw()
    {
        return "Unknown exception occurred.";
    }
};

class IO_Exception : public Exception
{
public:
    bool fileNotFound(const std::string &filename) const
    {
        // Check if the file exists and return true if not found
        return true;
    }
};

class Arithmetic_Exception : public Exception
{
public:
    bool divisionByZero(double divisor) const
    {
        // Check if the divisor is zero and return true if so
        return true;
    }
};

class Memory_Exception : public Exception
{
public:
    bool allocationError() const
    {
        // Check if the allocation was successful and return true if it failed
        return true;
    }
};

int main()
{
    IO_Exception io;
    if (io.fileNotFound("file.txt"))
    {
        std::cout << "File not found.\n";
    }

    Arithmetic_Exception arith;
    if (arith.divisionByZero(0))
    {
        std::cout << "Division by zero.\n";
    }

    Memory_Exception mem;
    if (mem.allocationError())
    {
        std::cout << "Error during dynamic memory allocation.\n";
    }

    return 0;
}
