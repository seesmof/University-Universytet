#include "../lib.h"

using namespace std;

int getMaxPoints(vector<vector<ll>> &matrix, int i, int j)
{
    // Base case
    if (i < 0 || j < 0)
        return 0;
    if (i >= matrix.size() || j >= matrix[0].size())
        return 0;

    // Recursive Case
    return matrix[i][j] + max(getMaxPoints(matrix, i - 1, j),
                              getMaxPoints(matrix, i, j + 1));
}

int main()
{
    srand((unsigned)time(NULL));
    ll t;
    cin >> t;
    while (t--)
    {
        cout << endl;
        ll n;
        cout << BOLD << "\nEnter a size: " << UNBOLD;
        cin >> n;
        vector<vector<ll>> matrix;
        for (int i = 0; i < n; i++)
        {
            vector<ll> row;
            for (int j = 0; j < n; j++)
            {
                ll element = rand() % 10;
                row.pb(element);
            }
            matrix.pb(row);
        }
        outputArray(matrix);

        ll I, J;
        cout << GRAY << "\nEnter finish point: " << UNGRAY;
        cin >> I >> J;
        I--;
        J--;

        int points = getMaxPoints(matrix, I, J);

        cout << YELLOW << "\nThe maximum number of points achievable is: " << points << endl
             << UNYELLOW;
    }

    return 0;
}