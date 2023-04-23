```c++
#include <iostream>
#include <fstream>
// Base Exception class
class Exception {
public:
virtual const char* what() const throw() {
return "An exception has occurred";
}
};
// Exception class for handling I/O stream errors
class IOException : public Exception {
public:
const char* what() const throw() override {
return "I/O stream error";
}
};
// Exception class for handling arithmetic errors (division by 0)
class ArithmeticException : public Exception {
public:
const char* what() const throw() override {
return "Arithmetic error: division by zero";
}
};
// Exception class for handling errors in dynamic memory allocation
class MemoryException : public Exception {
public:
const char* what() const throw() override {
return "Memory allocation error";
}
};
// Example function that uses the above-defined exception classes
void divide(int a, int b) {
if (b == 0) {
throw ArithmeticException();
}
std::cout << "Result: " << a / b << std::endl;
}
int main() {
try {
// Example of handling I/O stream error
std::ifstream file("nonexistent_file.txt");
if (!file.is_open()) {
throw IOException();
}
// Example of handling arithmetic error
divide(10, 0);
// Example of handling memory allocation error
int* arr = new int[1000000000000];
delete[] arr;
}
catch (Exception& e) {
std::cerr << "Exception caught: " << e.what() << std::endl;
}
return 0;
}
```
