#include <iostream>
#include <Windows.h>
#include <vector>

std::vector<std::string> getListOfDrives()
{
    std::vector<std::string> arrayOfDrives;
    char *szDrives = new char[MAX_PATH]();
    if (GetLogicalDriveStringsA(MAX_PATH, szDrives))
        ;
    for (int i = 0; i < 100; i += 4)
        if (szDrives[i] != (char)0)
            arrayOfDrives.push_back(std::string{szDrives[i], szDrives[i + 1], szDrives[i + 2]});
    delete[] szDrives;
    return arrayOfDrives;
}

int main()
{
    std::vector<std::string> drives = getListOfDrives();

    for (std::string currentDrive : drives)
    {
        std::cout << currentDrive << std::endl;
    }

    auto system_disk = L"C:\\";
    std::cout << GetDiskFreeSpace() << std::endl;
}