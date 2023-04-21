// include necessary libraries
#pragma once
#include <bits/stdc++.h>
#include "lib.cpp"
using namespace std;

ll showMenu(const vector<string> &menuOptions)

    // for transforming string to lowercase
    string toLower(string str);

// for outputting error messages
void bad(const string &INPUT);

// for outputting success messages
void good(const string &INPUT);

// get number input from user and validate it
ll getNum();

// validates an inputed name
string validateName(string inputString);

// implements the Quick Sort algorithm to sort the elements of the given vector in ascending order
template <typename T>
void quickSort(vector<T> &arr, int left, int right);

// implements the Exchange Sort algorithm to sort the elements of the given vector in ascending order
template <typename T>
void exchangeSort(vector<T> &arr);

// implements the Bubble Sort algorithm to sort the elements of the given vector in ascending order
template <typename T>
void bubbleSort(vector<T> &arr);

// implements the Merge Sort algorithm to sort the elements of the given vector in ascending order
template <typename T>
void mergeSort(vector<T> &arr);

// to output one dimensional vector
template <typename T>
void outputArray(vector<T> arr);

// to output one dimensional array
void outputArray(int *arr);

// to output two dimensional vector
void outputArray(vector<vector<int>> &arr);

// for getting email address from user
string getEmailAddress();

// For getting text file inputted from user
string getFileName();

// For generating a random string of given length
string generateRandomString(int length);

// For generating a random password of given length
string generateRandomPassword(int length);

// returns a vector containing only the unique elements from the input vector
vector<string> getUniqueVector(vector<string> &inputVector);

// For making text bold
ostream &BOLD(ostream &os);

// For changing text back to normal
ostream &UNBOLD(ostream &os);

// For setting text color to red
ostream &RED(ostream &os);

// For changing text back to normal
ostream &UNRED(ostream &os);

// For setting text color to green
ostream &GREEN(ostream &os);

// For changing text back to normal
ostream &UNGREEN(ostream &os);

// For changing text color to gray
ostream &GRAY(ostream &os);

// For changing text back to normal
ostream &UNGRAY(ostream &os);

// For changing text color to yellow
ostream &YELLOW(ostream &os);

// For changing text back to normal
ostream &UNYELLOW(ostream &os);