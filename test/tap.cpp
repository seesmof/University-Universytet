#include <iostream>
#include <fstream>
using namespace std;

int main()
{
    ofstream ofs("out.txt");
    if (ofs.is_open())
    {
        cout << "File must be opened\n";
        ofs << "testing this thing...\n";
        ofs << "========================================\n";
        ofs << "Welcome on board!\n";
        ofs << "========================================\n";
        ofs.close();
    }
    else
    {
        cout << "ERROR: Couldn't open output file!\n";
        return -1;
    }

    return 0;
}
