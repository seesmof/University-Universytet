#include <iostream>
#include <Windows.h>
#include <vector>

int main()
{
	DWORD res = GetLogicalDrives();
	std::cout << res << " " << type_info(res);
	std::cout << GetLogicalDrives();
}