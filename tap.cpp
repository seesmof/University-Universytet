#include <bits/stdc++.h>
using namespace std;
int main()
{
    long long n, a, b, s = 0, t = 0, p = 0;
    cin >> n;
    vector<long long> v;
    for (long long i = 0; i < 2 * n; i++)
    {
        cin >> a >> b;
        s += a;
        long long t = b - a;
        v.push_back(t);
    }
    sort(v.begin(), v.end());
    for (long long i = v.size() - 1; i >= 0; i--)
    {
        t++;
        p += v[i];
        if (t == n)
        {
            break;
        }
    }
    cout << s + p;
}