#include <bits/stdc++.h>
using namespace std;

const int dx[] = {1, 0, -1, 0}, dy[] = {0, 1, 0, -1}; // possible movements in x and y directions

vector<vector<int>> shortestPath(vector<vector<int>> &grid, int startX, int startY, int endX, int endY)
{
    int n = grid.size(), m = grid[0].size();
    vector<vector<int>> dist(n, vector<int>(m, -1)); // initialize distance to -1
    queue<pair<int, int>> q;
    dist[startX][startY] = 0;
    q.push({startX, startY});
    while (!q.empty())
    {
        auto [x, y] = q.front();
        q.pop();
        for (int i = 0; i < 4; i++)
        {
            int a = x + dx[i], b = y + dy[i];
            if (a >= 0 && a < n && b >= 0 && b < m && grid[a][b] == 0 && dist[a][b] == -1)
            {
                dist[a][b] = dist[x][y] + 1;
                q.push({a, b});
            }
        }
    }
    return dist;
}

int main()
{
    srand((unsigned)time(NULL));
    int i, j;
    cout << "Enter size of grid (N M): ";
    cin >> i >> j;
    vector<vector<int>> grid;

    cout << "\nYour initial matrix: \n";
    for (int k = 0; k < i; k++)
    {
        vector<int> row;
        for (int m = 0; m < j; m++)
        {
            int element = rand() % 10;
            row.push_back(element);
            cout << element << " ";
        }
        grid.push_back(row);
        cout << endl;
    }

    int sI = 0, sJ = j - 1;
    int eI, eJ;
    cout << "Enter ending point coordinates (Y X): ";
    cin >> eI >> eJ;
    vector<vector<int>> res = shortestPath(grid, 0, 0, eJ, eI);

    cout << "\nResulting matrix: \n";
    for (int k = 0; k < i; k++)
    {
        for (int m = 0; m < j; m++)
        {
            cout << res[k][m] << " ";
        }
        cout << endl;
    }
}