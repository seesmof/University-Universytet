#include <iostream>
#include <math.h>

using namespace std;

int main(int argc, char **argv)
{
    double height, weight;
    double bmi;

    cout << "Enter your height: " << endl;
    cin >> height;

    cout << "Enter your weight: " << endl;
    cin >> weight;

    bmi = (weight) / (pow(height, 2));

    if (bmi <= 18.4)
    {
        cout << "Your BMI is " << bmi << ". You are underweight and should definitely gain some weight." << endl;
    }
    else if (bmi >= 18.5 && bmi <= 24.9)
    {
        cout << "Your BMI is " << bmi << ". You have a normal weight, keep it up!" << endl;
    }
    else if (bmi >= 25 && bmi <= 39.9)
    {
        cout << "Your BMI is " << bmi << ". You have some excess weight, get some workouts going." << endl;
    }
    else if (bmi >= 40)
    {
        cout << "Your BMI is " << bmi << ". You are obese and should definitely do something about your weight." << endl;
    }

    return 0;
}