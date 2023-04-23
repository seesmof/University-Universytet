#pragma once
#include "exc.cpp"
#include "D:\repos\university\lib.h"

class Exception;
class IOException : public Exception
{
};
class ArithmeticException : public Exception
{
};
class MemoryException : public Exception
{
};