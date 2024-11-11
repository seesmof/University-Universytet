#include <iostream>
#include <Windows.h>

int main()
{
    LPCWSTR drive_name=L"C:\\";
    UINT drive_type=GetDriveType(drive_name);
    std::cout << "Drive type " << drive_type << std::endl;
}