#pragma once
#include "sup.cpp"
#include "D:\repos\university\lib.h"

class DynamicString;

void showStrings(const vector<DynamicString> &container);

void showStrings(vector<DynamicString> &container, const string &OUTPUT_FILENAME);

void addStrings(vector<DynamicString> &container);

void addStrings(vector<DynamicString> &container, const string &INPUT_FILENAME);

void removeString(vector<DynamicString> &container);

void outputMenu(vector<DynamicString> &container);