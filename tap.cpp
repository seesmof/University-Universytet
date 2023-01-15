#include <iostream>
#include <vector>
using namespace std;

// Function to find the maximum points from given matrix
int maxPoints(vector<vector<int>> matrix, int row, int col)
{
    // Base case: If the starting point is the finish point, return its value
    if (row == 0 && col == 0)
        return matrix[row][col];

    // If the starting point is not the finish point, then recursively calculate the maximum points from each direction (left and down) and return the maximum of them.
    if (row > 0 && col > 0)
    {
        int left = maxPoints(matrix, row - 1, col); // Maximum points from left direction
        int down = maxPoints(matrix, row, col - 1); // Maximum points from down direction

        return max(left + matrix[row][col], down + matrix[row][col]); // Return maximum of both directions.
    }
    else if (row > 0)
    { // If only left direction is available.

        return maxPoints(matrix, row - 1, col) + matrix[row][col];
    }
    else if (col > 0)
    { // If only down direction is available.

        return maxPoints(matrix, row, col - 1) + matrix[row][col];
    }
    else
    { // No direction is available.

        return 0;
    }
}

// Driver code to test above function.
int main()
{
    // 3x3 Matrix with points in each cell.
    vector<vector<int>> matrix;
    for (int i = 0; i < 3; i++)
    {
        vector<int> row;
        for (int j = 0; j < 3; j++)
        {
            int element = rand() % 10;
            row.push_back(element);
            cout << element << " ";
        }
        matrix.push_back(row);
        cout << endl;
    }

    int row, col;
    cout << "\nEnter finish point (Row Col): ";
    cin >> row >> col;
    cout << "Maximum Points: " << maxPoints(matrix, row, col);
    return 0;
}