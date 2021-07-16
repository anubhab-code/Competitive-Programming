#include <iostream>
#include <algorithm>

using namespace std;

const int N = 3 * 1e5 + 10;

int n;
int a[N];

int h(int i)
{
    return (i > 0 && i < n - 1 && a[i] > a[i - 1] && a[i] > a[i + 1]) ? 1 : 0;
}

int v(int i)
{
    return (i > 0 && i < n - 1 && a[i] < a[i - 1] && a[i] < a[i + 1]) ? 1 : 0;
}

int main()
{
    int tt;
    cin >> tt;
    while (tt--)
    {
        int c = 0;
        cin >> n;
        for (int i = 0; i < n; i++)
            cin >> a[i];
        for (int i = 1; i < n - 1; i++)
            if (h(i) || v(i))
                c++;
        int ans = c;
        for (int i = 1; i < n - 1; i++)
        {
            int original = a[i];
            int x = c - (h(i) + h(i - 1) + h(i + 1) + v(i) + v(i - 1) + v(i + 1));
            a[i] = a[i + 1];
            ans = min(ans, x + (h(i) + h(i - 1) + h(i + 1) + v(i) + v(i - 1) + v(i + 1)));
            a[i] = a[i - 1];
            ans = min(ans, x + (h(i) + h(i - 1) + h(i + 1) + v(i) + v(i - 1) + v(i + 1)));
            a[i] = original;
        }
        cout << ans << "\n";
    }
    return 0;
}
