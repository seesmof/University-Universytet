#pragma once
#include <bits/stdc++.h>
#include "sup.cpp"
#include "../../lib.h"
using namespace std;

class DynamicString;

// define an output stream operator function
ostream &operator<<(ostream &outputStream, const DynamicString &OUTPUT);

// define an input stream operator function
istream &operator>>(istream &inputStream, DynamicString &inputHolder);

// define an output stream operator function for file
ofstream &operator<<(ofstream &outputStream, const DynamicString &OUTPUT);

// define an input stream operator function for file
ifstream &operator>>(ifstream &inputStream, DynamicString &inputHolder);

// for showing the main menu of the application
void outputMenu(vector<DynamicString> &container);