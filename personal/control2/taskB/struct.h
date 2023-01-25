// include necessary libraries
#include <bits/stdc++.h>
using namespace std;

#pragma once

// create struct for holding emails data
struct Letter
{
    string outAddress;
    string inAddress;
    string recievedDate;
    string letterHeading;
    string letterText;
    int letterSize;
    bool isRead;
};

// for filling in the vector of emails
void fillVector(vector<Letter> &a, const string &FILE_NAME)
{
    // declare local variables
    fstream inFile(FILE_NAME.c_str(), ios::in);
    string lineReader;
    int numOfLetters = 1;
    vector<string> linesHolder;

    // check if we cannot read the file
    if (!inFile.is_open())
    {
        cout << "ERROR: Could not open file " << FILE_NAME << endl;
        return;
    }

    // read every line from the file
    while (getline(inFile, lineReader))
    {
        // when found empty line increase line number
        if (lineReader.empty())
            numOfLetters++;
        // in other cases add the line into a vector
        else
            linesHolder.push_back(lineReader);
    }

    // create a loop for sorting out each line and placing them into a correct spot
    for (int i = 0, j = 0; i < numOfLetters; i++, j += 5)
    {
        // create instance of struct in vector
        a.push_back(Letter());

        // fill out all the data from file
        a[i].outAddress = linesHolder[j];
        a[i].inAddress = linesHolder[j + 1];
        a[i].recievedDate = linesHolder[j + 2];
        a[i].letterHeading = linesHolder[j + 3];
        a[i].letterText = linesHolder[j + 4];

        // count words in letter text using another loop
        int lenHolder = 1;
        string strHolder = a[i].letterText;
        for (int i = 0; i < strHolder.length(); i++)
            if (strHolder[i] == ' ')
                lenHolder++;

        // add words count and status to vector as well
        a[i].letterSize = lenHolder;
        a[i].isRead = false;
    }

    // end function
    return;
}