// include necessary libraries
#include <bits/stdc++.h>
using namespace std;

#pragma once

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

    // should not reach this point
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
    string chars = "ABCDEFGHIJKLMNOPQRSTUVWXYabcdefghijklmnopqrstuvwxy"; // characters pool to generate random string from
    string randomString = "";                                            // random string result holder

    // Generate a random character and add it to the string until it reaches the desired length
    for (int i = 0; i < length; i++)
    {
        // Generate a random index between 0 and the size of our character pool
        int index = rand() % chars.size();

        // Add the character at that index to our string
        randomString += chars[index];
    }

    return randomString + ".txt"; // Append ".txt" and return the generated string
}

// returns a vector containing only the unique elements from the input vector
vector<string> getUniqueElements(vector<string> &inputVector)
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