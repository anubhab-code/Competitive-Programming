#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

int main()
{
    ll tt;
    cin >> tt;
    while (tt--)
    {
        ll a, b;
        cin >> a >> b;
        ll res = 1 + a / b;
        for (ll i = b; i <= b + 100; i++)
        {
            if (i == 1)
                continue;
            ll div = 0, cur = a;
            while (cur)
            {
                cur /= i;
                div++;
            }
            ll count = (i - b) + div;
            if (res >= count)
                res = count;
        }
        cout << res << endl;
    }
    return 0;
}