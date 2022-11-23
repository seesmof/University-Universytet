// include necessary libraries
#include <iostream>
#include <string>
using namespace std;

// create a structure to hold the semi truck's information
struct freightTruck
{
    string manufacturerName;
    string modelName;
    int carryingCapacity;
    int manufacturedYear;
    int registrationYear;
};

// declare a function prototype
void trucksInput(int n, freightTruck *truck);

// declare main function
int main(int argc, char **argv)
{
    // output program intro
    system("cls");
    cout << "****************************** Task A *************************************" << endl
         << endl;

    // declare local variables
    int n;
    freightTruck truck[n];

    // ask user to enter the amount of trucks he wants
    cout << "Enter the amount of truck you want to enter: ";
    cin >> n;
    // call a function for entering information for each of the trucks
    trucksInput(n, truck);

    // create function to output the trucks that suit the parameters
    cout << endl;
    for (int i = 0; i < n; i++)
    {
        // if truck's registration year is less than 2021 and it has a carrying capacity of more than 3 tons
        if (truck[i].registrationYear < 2021 && truck[i].carryingCapacity > 3)
        {
            // output its information to user
            cout << truck[i].manufacturerName << " " << truck[i].modelName << " has carrying capacity of " << truck[i].carryingCapacity << " tons, was manufactured in " << truck[i].manufacturedYear << " and registered in " << truck[i].registrationYear << "." << endl;
        }
    }

    // output project outro
    cout << endl
         << "***************************************************************************" << endl;

    // end main function
    return 0;
}

// create function that will ask user to input information for each of the vehicles
void trucksInput(int n, freightTruck *truck)
{
    // create for loop for the amount of vehicles a user entered before
    for (int i = 0; i < n; i++)
    {
        // ask user to enter manufacturerName
        cout << i + 1 << ". Enter manufacter name: ";
        cin >> truck[i].manufacturerName;
        // if the name starts with a lowercase letter
        if (islower(truck[i].manufacturerName[0]))
        {
            // convert it to an uppercase one
            truck[i].manufacturerName[0] = toupper(truck[i].manufacturerName[0]);
        }
        // ask user to enter modelName
        cout << i + 1 << ". Enter model name: ";
        cin >> truck[i].modelName;
        // ask user to enter carryingCapacity
        cout << i + 1 << ". Enter carrying capacity: ";
        cin >> truck[i].carryingCapacity;
        // ask user to enter manufacturedYear
        cout << i + 1 << ". Enter manufactured year: ";
        cin >> truck[i].manufacturedYear;
        // ask user to enter registrationYear
        cout << i + 1 << ". Enter registration year: ";
        cin >> truck[i].registrationYear;
        cout << endl;
    }
    // end function
    return;
}