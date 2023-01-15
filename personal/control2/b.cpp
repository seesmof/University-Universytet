// include necessary libraries
#include <bits/stdc++.h>
using namespace std;

class Email
{
private:
    string senderEmail;      // Sender's email address
    string recipientEmail;   // Recipient's email address
    time_t dateTimeSent;     // Date and time of sending
    string messageHeader;    // Message header (subject, etc.)
    int messageSize;         // Message size in bytes
    string messageShortText; // Short text of the message (first few lines)
    bool statusRead;         // Status - read or not

public:
    Email(string senderEmail, string recipientEmail, time_t dateTimeSent, string messageHeader, int messageSize, string messageShortText);

    void setSenderEmail(string senderEmail);           // Set sender's email address
    void setRecipientEmail(string recipientEmail);     // Set recipient's email address
    void setDateTimeSent(time_t dateTimeSent);         // Set date and time of sending
    void setMessageHeader(string messageHeader);       // Set message header (subject, etc.)
    void setMessageSize(int messageSize);              // Set message size in bytes
    void setMessageShortText(string messageShortText); // Set short text of the message (first few lines)

    string getSenderEmail();      // Get sender's email address
    string getRecipientEmail();   // Get recipient's email address
    time_t getDateTimeSent();     // Get date and time of sending
    string getMessageHeader();    // Get message header (subject, etc.)
    int getMessageSize();         // Get message size in bytes
    string getMessageShortText(); // Get short text of the message (first few lines)

    bool isRead(); // Check if the status is read or not

    void sendMessage(); // Send the formatted email.
};

struct letterData
{
    string senderEmail;
    string receiverEmail;
    string sentDate;
    string sentTime;
    string messageHeader;
    int numOfWords;
    string messageText;
    bool isRead;
};

// function prototypes //
string fileNameInput();
string randString(int);
int countLetters(const string &);
void fillArray(const string &, letterData *);
void showMessages(letterData *, int);
/////////////////////////

// func main start
int main()
{
    // declare local variables //
    srand(time(NULL));
    char doContinue;
    int userDecision;
    /////////////////////////////

    // project intro
    cout << "\n/////////////////////////////////////////////////////////////\n"
         << "\nWelcome! This program will manipulate messages.\n";
    string inputFileName = fileNameInput();
    cout << "\n/////////////////////////////////////////////////////////////\n\n";
    do
    {
        //////////////////////////////////////////////////////////////////////////////////
        int numOfLetters = countLetters(inputFileName);
        letterData *letter = new letterData[numOfLetters];
        fillArray(inputFileName, letter);
        showMessages(letter, numOfLetters);

        cout << "Choose an action you would like to perform" << endl;
        //////////////////////////////////////////////////////////////////////////////////
        cout << "\n/////////////////////////////////////////////////////////////\n"
             << "\nWould you like to continue program execution? (Y | N): ";
        cin >> doContinue;
        if (doContinue == 'Y' || doContinue == 'y')
        {
            cout << "\n/////////////////////////////////////////////////////////////\n\n";
            continue;
        }
        else
            break;
    } while (doContinue = 'Y' || doContinue == 'y');

    // func main end
    cout << "\nThanks for using this program\n"
         << "\n/////////////////////////////////////////////////////////////\n\n";
    return 0;
}

void showMessages(letterData *data, int n)
{
    cout << endl
         << "Messages in your inbox: " << endl;
    cout << "======================================" << endl;
    for (int i = 0, j = 0; i < n; i++, j += 6)
    {
        cout << endl;
        cout << "From " << data[i].senderEmail << endl;
        cout << "To " << data[i].receiverEmail << endl;
        cout << endl
             << "Sent " << data[i].sentDate << " " << data[i].sentTime << endl;
        cout << "======================================" << endl;
        cout << data[i].messageHeader << endl
             << endl;
        cout << data[i].messageText << endl;
        cout << endl
             << data[i].numOfWords << " words" << endl;
        cout << "======================================" << endl;
        cout << "Message read" << endl
             << endl;
    }
}

// function to fill in the struct array
void fillArray(const string &filename, letterData *arr)
{
    // declare local variables
    fstream f(filename.c_str()); // for storing the input file
    string line;                 // for storing the current line
    vector<string> lines;        // for storing all the lines
    int letters = 1;             // for storing the number of letters

    // get all the lines from the input file
    while (getline(f, line))
    {
        // if given line is empty
        if (line.empty())
        {
            // increment letters counter
            letters++;
            // jump to the next iteration
            continue;
        }
        // add line to the lines array
        lines.push_back(line);
    }

    // create for loop for filling in the struct array
    for (int i = 0, j = 0; i < letters; i++, j += 6)
    {
        // add sender email address
        arr[i].senderEmail = lines[j];
        // add receiver email address
        arr[i].receiverEmail = lines[j + 1];
        // add sent date
        arr[i].sentDate = lines[j + 2];
        // add sent time
        arr[i].sentTime = lines[j + 3];
        // add message header
        arr[i].messageHeader = lines[j + 4];

        // declare a holder for message text
        string holder = lines[j + 5];
        // for storing word count of the message
        int wordCount = 1;
        // create for loop for counting words
        for (int k = 0; k < holder.size(); k++)
            // if found a space
            if (holder[k] == ' ')
                // increment word count
                wordCount++;

        // add number of words
        arr[i].numOfWords = wordCount;
        // add message text
        arr[i].messageText = holder;
        // set message status to read
        arr[i].isRead = true;
    }

    // end function execution
    return;
}

int countLetters(const string &filename)
{
    int res = 1;
    fstream f(filename.c_str(), ios::in);

    string line;
    while (getline(f, line))
    {
        if (line.empty())
        {
            res++;
            continue;
        }
    }

    return res;
}

// create a function that will take file name from user
string fileNameInput()
{
    // declare local variables
    bool isExtensionFound = false;
    string input;

    // ask user to input file name
    cout << "Enter the name of the file: ";
    cin >> input;
    cin.ignore();

    // create for loop to look for extension
    for (int i = 0; i < input.length(); i++)
    {
        // dot is an indication of extension
        if (input[i] == '.')
        {
            // if found then change bool isExtensionFound to true
            isExtensionFound = true;
            break; // break out of loop
        }
    }

    // if the result is not found then
    if (!isExtensionFound)
    {
        // create a new string for holding the file extension
        string fileExtension;

        // ask user to enter a file extension
        cout << "Please specify a file extension: ";
        cin >> fileExtension;
        cin.ignore();

        // create a for loop
        for (int i = 0; i < fileExtension.length(); i++)
        {
            // look for a dot in input
            if (fileExtension[i] == '.')
            {
                // if found then add it to the result string
                input += fileExtension;
                break; // break out of loop
            }
            else
            {
                // if not found then add add a dot + input to the result string
                input += "." + fileExtension;
                break; // break out of loop
            }
        }
    }

    // return the result string
    return input;
}

// create a function that will generate random string
string randString(int ch)
{
    // declare max array length
    const int maxArrSize = 25;
    // declare possible characters
    char possibleCharactersArr[maxArrSize] = {'a', 'b', 'c', 'd', 'e', 'f', 'g',
                                              'h', 'i', 'j', 'k', 'l', 'm', 'n',
                                              'o', 'p', 'q', 'r', 's', 't', 'u',
                                              'v', 'w', 'x', 'y'};
    // declare result string
    string result = "";
    // create for loop
    for (int i = 0; i < ch; i++)
        // add random character from an earlier declared set to the string
        result += possibleCharactersArr[rand() % maxArrSize];

    // add file extension to result
    result += ".txt";
    // return result
    return result;
}