// include necessary libraries
#include <bits/stdc++.h>
#include "lib.h"
using namespace std;

#define ll long long
#define all(x) (x).begin(), (x).end()
#define pb push_back
#define eb emplace_back
#define mp make_pair
#define endl "\n"
void dbg_out()
{
    cerr << endl;
}
template <typename Head, typename... Tail>
void dbg_out(Head H, Tail... T)
{
    cerr << ' ' << H;
    dbg_out(T...);
}
#define dbg(...) cerr << "(" << #__VA_ARGS__ << "):", dbg_out(__VA_ARGS__)

// for outputting error messages
void bad(const string &INPUT)
{
    // create a stringstream object to store the message
    stringstream ss;
    // add ANSI escape codes for red text
    ss << "\033[1;31mERROR: " << INPUT << "\033[0m";
    // output the message to cerr
    cerr << ss.str() << endl;
}

// for outputting success messages
void good(const string &INPUT)
{
    // create a stringstream object to store the message
    stringstream ss;
    // add ANSI escape codes for red text
    ss << "\033[1;32mSUCCESS: " << INPUT << "\033[0m";
    // output the message to cerr
    cerr << ss.str() << endl;
}

// for getting nubmer input from user
ll getNum()
{
    // declare variables for holding the input
    ll number;
    // while user enters invalid input
    while (!(cin >> number))
    {
        // clear buffer
        cin.clear();
        // ignore new line char
        cin.ignore(256, '\n');
        // output error message and continue
        cout << endl;
        bad("Enter an integer");
        cout << endl;
    }
    return number;
}

// For making text bold
ostream &BOLD(ostream &os)
{
    return os << "\e[1m";
}

// For changing text back to normal
ostream &UNBOLD(ostream &os)
{
    return os << "\e[0m";
}

// For setting text color to red
ostream &RED(ostream &os)
{
    return os << "\033[1;31m";
}

// For changing text back to normal
ostream &UNRED(ostream &os)
{
    return os << "\033[0m";
}

// For setting text color to green
ostream &GREEN(ostream &os)
{
    return os << "\033[1;32m";
}

// For changing text back to normal
ostream &UNGREEN(ostream &os)
{
    return os << "\033[0m";
}

// For changing text color to gray
ostream &GRAY(ostream &os)
{
    return os << "\033[1;30m";
}

// For changing text back to normal
ostream &UNGRAY(ostream &os)
{
    return os << "\033[0m";
}

// For changing text color to yellow
ostream &YELLOW(ostream &os)
{
    return os << "\033[1;33m";
}

// For changing text back to normal
ostream &UNYELLOW(ostream &os)
{
    return os << "\033[0m";
}

ll showMenu(const vector<string> &MENU_OPTIONS)
{
    cout << BOLD << "Welcome! Choose one option from the menu below\n"
         << UNBOLD;
    for (ll i = 0; i < MENU_OPTIONS.size(); i++)
    {
        cout << i + 1 << ". " << MENU_OPTIONS[i] << endl;
    }
    cout << "Enter your choice: ";
    ll userDecision = getNum();
    cout << endl;
    return userDecision;
}

string toLower(string str)
{
    // transfort the whole stirng
    transform(str.begin(), str.end(), str.begin(), ::tolower);
    // return it
    return str;
}

// validates an inputed name
string validateName(string inputString)
{
    stringstream stringProcessor(inputString); // create a stringstream object from the inputted name
    string wordHolder;
    string resultHolder;

    while (stringProcessor >> wordHolder)
    { // loop through each word in the stringstream
        if (!isupper(wordHolder[0]))
        {                                           // check if the first letter of the word is not uppercase
            wordHolder[0] = toupper(wordHolder[0]); // capitalize the first letter of the word
        }
        resultHolder += wordHolder + " "; // add the modified word to the new name
    }
    return resultHolder; // return the result of the validation
}

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
template <typename T>
void outputArray(vector<vector<T>> &arr)
{
    int n = arr.size();
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
            cout << arr[i][j] << " ";
        cout << "\n";
    }
}

// for getting email address from user
string getEmailAddress()
{
    // ask user for email address
    string emailAddress;
    cout << "Please enter an email address: ";
    cin >> emailAddress;

    // validate email address
    if (emailAddress.find("@") == string::npos)
    {
        cout << "\nERROR: Invalid email address\n\n";
        getEmailAddress();
    }
    else
        return emailAddress;

    // should not reach this pointt
    return "";
}

// For getting text file inputted from user
string getFileName()
{
    // Declare local variables
    string fileName = "";         // for storing file name
    bool isExtensionFound = true; // for tracking file extension

    // Create do while loop for properly getting file name with extension
    do
    {
        // Ask user to enter file name
        cout << "Enter file name: ";
        cin >> fileName;

        // Create condition to check if file extension is found
        if (fileName.find(".") == string::npos)
        {
            // Execute if not found
            isExtensionFound = false; // set tracker state to false
            // Output error message
            cout << "\nERROR: File extension not found. Try again...\n\n";
            continue; // jump into next iteration
        }
        // If extension is found
        else
            break; // jump out of loop
    } while (isExtensionFound == false);

    // Return file name
    return fileName;
}

// For generating a random string of given length
string generateRandomString(int length)
{
    // Declare local variables
    string chars = "abcdefghijklmnopqrstuvwxy"; // characters pool to generate random string from
    string randomString = "";                   // random string result holder

    // Generate a random character and add it to the string until it reaches the desired length
    for (int i = 0; i < length; i++)
    {
        // Generate a random index between 0 and the size of our character pool
        int index = rand() % chars.size();

        // Add the character at that index to our string
        randomString += chars[index];
    }

    return randomString; // Append ".txt" and return the generated string
}

// For generating a random password of given length
string generateRandomPassword(int length)
{
    // Declare local variables
    string chars = "ABCDEFGHIJKLMNOPQRSTUVWXYabcdefghijklmnopqrstuvwxy1234567890!@#$%^&*()_+=-[]{}`~';/.,"; // characters pool to generate random string from
    string randomPass = "";                                                                                 // random string result holder

    // Generate a random character and add it to the string until it reaches the desired length
    for (int i = 0; i < length; i++)
    {
        // Generate a random index between 0 and the size of our character pool
        int index = rand() % chars.size();

        // Add the character at that index to our string
        randomPass += chars[index];
    }

    return randomPass;
}

// returns a vector containing only the unique elements from the input vector
vector<string> getUniqueVector(vector<string> &inputVector)
{
    vector<string> uniqueElements;      // to store unique elements as strings
    unordered_set<string> seenElements; // to store elements that have already been seen

    // iterate through each element of the inputVector
    for (string element : inputVector)
    {
        // check if the element is present in the seenElements container
        if (seenElements.find(element) == seenElements.end())
        {
            uniqueElements.push_back(element); // add the element to uniqueElements vector
            seenElements.insert(element);      // inserts the element into the seenElements set, if it is not already present
        }
    }

    // return a vector containing only the unique elements from the original vector
    return uniqueElements;
}
