#include <bits/stdc++.h>
#include "../lib.h"
using namespace std;

class Store
{
private:
    vector<ll> values;

public:
    Store() : values(NULL) {}

    void Insert(ll value)
    {
        for (ll i = 0; i < values.size(); i++)
        {
            if (values[i] == value)
            {
                bad("Value already exists in store");
                return;
            }
        }
        values.eb(value);
    }

    void Remove(ll value)
    {
        for (ll i = 0; i < values.size(); i++)
        {
            if (values[i] == value)
            {
                good("Value successfully removed");
                values.erase(values.begin() + i);
            }
        }
    }

    ll Get() const
    {
        ll result = rand() % values.size();
        return values[result];
    }

    ll Size() const
    {
        return values.size();
    }

    void Output() const
    {
        for (ll i = 0; i < values.size(); i++)
            cout << values[i] << endl;
    }
};

// func main start
int main()
{
    // declare local variables //
    srand(time(NULL));
    char doContinue;
    /////////////////////////////

    ///////////////////////////////////////
    Store store;

    store.Output();

    cout << "\nEnter how many elements to add";
    ll numToAdd = getNum();
    cout << "\nMake sure the elemnts are unique\n";
    for (ll i = 0; i < numToAdd; i++)
    {
        cout << "- ";
        ll value = getNum();
        store.Insert(value);
    }

    store.Output();

    cout << "Enter value to delete: ";
    ll value = getNum();

    store.Remove(value);

    store.Output();

    ///////////////////////////////////////

    // stop main function execution
    cout << "\nThanks for using this program\n\n";
    return 0;
}