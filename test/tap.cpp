#include "../lib.h"
using namespace std;

int main()
{
    string filename;
    ifstream inputFile;
    vector<string> lines;

    cout << "Enter the name of the input file: ";
    cin >> filename;

    inputFile.open(filename.c_str());

    if (!inputFile.is_open())
    {
        cout << "Unable to open file!";
        return 1;
    }

    string line;
    while (getline(inputFile, line))
    {
        lines.push_back(line);
    }

    inputFile.close();

    for (int i = 0; i < lines.size(); i++)
        cout << lines[i] << endl;

    string outputFileName = generateRandomString(4) + ".txt";
    cout << outputFileName << endl;
    fstream output(outputFileName.c_str(), ios::out);
    output.open(outputFileName.c_str(), ios::out);
    for (int i = 0; i < lines.size(); i++)
        output << lines[i] << endl;
    output.close();
    return 0;
}