#include "../lib.h"
#include <fstream>
using namespace std;

int main()
{
    ofstream ofs("D:/repos/university/out.txt");
    if (ofs.is_open())
    {
        cout << "File must be opened\n";
        ofs << "testing this thing...\n";
        ofs << "========================================\n";
        ofs << setw(30) << "Welcome on board!\n";
        ofs << "========================================\n";
        ofs.close();
    }
    else
    {
        bad("Couldn't open output file!");
        return -1;
    }

    return 0;
}
