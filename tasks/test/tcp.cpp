#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <cmath>
#include <climits>
#include <cstdio>
#include <sstream>

using namespace std;

#define ll long long
#define pii pair<int, int>
#define pll pair<ll, ll>
#define pdd pair<double, double>
#define pb push_back
#define mp make_pair
#define ull unsigned long long
#define endl "\n"
#define ios                           \
    ios_base::sync_with_stdio(false); \
    cin.tie(NULL);                    \
    cout.tie(NULL);

template <class T>
T max(T a, T b, T c)
{
    return max(a, max(b, c));
}

template <class T>
T min(T a, T b, T c)
{
    return min(a, min(b, c));
}

template <class T>
T gcd(T a, T b)
{
    if (b == 0)
        return a;
    return gcd(b, a % b);
}

template <class T>
T lcm(T a, T b)
{
    return a * b / gcd(a, b);
}

template <class T>
T to_int(const T &x)
{
    stringstream ss;
    ss << x;
    T r;
    ss >> r;
    return r;
}

template <class T>
string to_str(const T &x)
{
    stringstream ss;
    ss << x;
    return ss.str();
}

template <class T>
void print_array(T arr[], int size_arr)
{
    for (int i = 0; i < size_arr; i++)
    {
        cout << arr[i] << " ";
    }
    cout << endl;
}

template <class T>
void print_vector(vector<T> v)
{
    for (int i = 0; i < v.size(); i++)
    {
        cout << v[i] << " ";
    }
    cout << endl;
}

template <class T>
void memset_array(T arr[], T value, int size_arr)
{
    for (int i = 0; i < size_arr; i++)
    {
        arr[i] = value;
    }
}

void solve()
{
    ll n;
    cin >> n;
    vector<ll> arr(n);
    for (int i = 0; i < n; i++)
        cin >> arr[i];

    sort(arr.begin(), arr.end());
    cout << arr[n - 2] << endl;
}

int main()
{
    ios;
    solve();
    return 0;
}