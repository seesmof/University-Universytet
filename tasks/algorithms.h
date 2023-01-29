// include necessary libraries
#include <bits/stdc++.h>
using namespace std;

#pragma once

// implements the Quick Sort algorithm to sort the elements of the given vector in ascending order
template <typename T>
void quickSort(vector<T> &arr, int left, int right)
{
    int i = left, j = right;             // initialize two variables, i and j, to the values of left and right respectively.
    int pivot = arr[(left + right) / 2]; // find the pivot element by taking the average of the left and right

    // check if size of array is <= 1, if so stop function
    if (arr.size() <= 1)
        return;

    // iterate through the values of i and j
    while (i <= j)
    {
        // iterate through the array until finds an element that is greater than the pivot value
        while (arr[i] > pivot)
            i++; // increment i
        // iterate through the array until finds an element that is less than the pivot value
        while (arr[j] < pivot)
            j--; // decrement j

        // check if the value of i is <= j.
        if (i <= j)
        {
            // swap the values of arr[i] and arr[j], then increment i and decrement j
            swap(arr[i], arr[j]);
            i++;
            j--;
        }
    };

    // recursively sort the left part of the array
    if (left < j)
        quickSort(arr, left, j);
    // recursively sort the right part of the array
    if (i < right)
        quickSort(arr, i, right);
}

// implements the Exchange Sort algorithm to sort the elements of the given vector in ascending order
template <typename T>
void exchangeSort(vector<T> &arr)
{
    // check if size of array is <= 1, if so stop function
    if (arr.size() <= 1)
        return;

    for (int i = 0; i < arr.size() - 1; i++)
        for (int j = i + 1; j < arr.size(); j++)
            if (arr[i] < arr[j])
                swap(arr[i], arr[j]);
}

// implements the Bubble Sort algorithm to sort the elements of the given vector in ascending order
template <typename T>
void bubbleSort(vector<T> &arr)
{
    // check if size of array is <= 1, if so stop function
    if (arr.size() <= 1)
        return;

    for (int i = 0; i < arr.size(); i++)
        for (int j = 0; j < arr.size() - i - 1; j++)
            if (arr[j] < arr[j + 1])
                swap(arr[j], arr[j + 1]);
}

// implements the Merge Sort algorithm to sort the elements of the given vector in ascending order
template <typename T>
void mergeSort(vector<T> &arr)
{
    // check if size of array is <= 1, if so stop function
    if (arr.size() <= 1)
        return;

    vector<int> left, right;     // for partitioning the array
    int middle = arr.size() / 2; // calculate the middle index of the array

    // iterate through the array from start to middle and add each element to left vector
    for (int i = 0; i < middle; i++)
        left.push_back(arr[i]);
    // iterate through the array from middle to end and add each element to right vector
    for (int i = middle; i < arr.size(); i++)
        right.push_back(arr[i]);

    // recursively sort left and right vectors
    mergeSort(left);
    mergeSort(right);

    int i = 0, j = 0, k = 0; // declare indeces

    // iterate through the left and right vectors until the end of either vector
    while (i < left.size() && j < right.size())
    {
        if (left[i] > right[j])
        {
            arr[k] = left[i];
            i++;
        }
        else
        {
            arr[k] = right[j];
            j++;
        }
        k++;
    }

    // merge left and input vectors
    while (i < left.size())
    {
        arr[k] = left[i];
        i++;
        k++;
    }

    // merge right and input vectors
    while (j < right.size())
    {
        arr[k] = right[j];
        j++;
        k++;
    }
}

// to output one dimensional vector
template <typename T>
void outputArray(vector<T> arr)
{
    for (auto i : arr)
        cout << i << " ";
    cout << endl;
}

// to output one dimensional array
void outputArray(int *arr)
{
    int n = sizeof(arr) / sizeof(int);
    for (int i = 0; i < n; i++)
        cout << arr[i] << " ";
    cout << endl;
}

// to output two dimensional vector
void outputArray(vector<vector<int>> &arr)
{
    int n = arr.size();
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
            cout << arr[i][j] << " ";
        cout << "\n";
    }
}