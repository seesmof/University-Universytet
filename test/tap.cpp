#include "../lib.h"

class DynArray
{
private:
    unsigned int *arr;
    int n;

public:
    DynArray(int count);
    ~DynArray();
    DynArray(const DynArray &obj);
    void show();
    void toFile();
    void fromFile();
};

istream &insetup(istream &ifs)
{
    ifs.setf(ios::scientific | ios::skipws | ios::hex);
    return ifs;
}

ostream &outsetup(ostream &ofs)
{
    ofs.fill(' ');
    ofs << setw(4);
    return ofs;
}

DynArray::DynArray(int count)
{
    n = count;
    arr = new unsigned int[n];
    for (int i = 0; i < n; i++)
        arr[i] = i;
}

DynArray::~DynArray() { delete[] arr; }

DynArray::DynArray(const DynArray &obj)
{
    n = obj.n;
    arr = new unsigned int[n];
    for (int i = 0; i < n; i++)
        arr[i] = obj.arr[i];
}

void DynArray::show()
{
    for (int i = 0; i < n; i++)
        cout << arr[i] << " ";
    cout << endl;
}

void DynArray::toFile()
{
    ofstream ofs("1.txt");
    if (ofs.is_open())
    {
        ofs << n << " ";
        for (int i = 0; i < n; i++)
        {
            ofs << outsetup << arr[i] * 2 << " ";
        }
    }
    ofs.close();
}

void DynArray::fromFile()
{
    ifstream ifs("1.txt");
    if (ifs.is_open())
    {
        ifs >> n;
        arr = new unsigned int[n];
        for (int i = 0; i < n; i++)
        {
            ifs >> insetup >> arr[i];
        }
    }
    ifs.close();
}

int main()
{
    DynArray obj1(5);
    obj1.show();
    obj1.toFile();
    obj1.fromFile();
    obj1.show();
    cin.get();
    return 0;
}