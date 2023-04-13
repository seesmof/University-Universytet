#pragma once
#include <bits/stdc++.h>
#include "sup.cpp"
#include "../../../lib.h"
using namespace std;

// delta class declaration
template <typename T>
class Delta;

// object deletion function
void deleteObjects(vector<unique_ptr<Delta<int>>> &deltaObjectsVector);

// object creation function
void createObjects(vector<unique_ptr<Delta<int>>> &deltaObjectsVector);

// printing objects function
void printObjects(vector<unique_ptr<Delta<int>>> &deltaObjectsVector);
