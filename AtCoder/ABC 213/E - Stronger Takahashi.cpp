#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define pll pair<ll, ll>
#define fi first
#define se second
#define pb push_back

const int N = 3e5+5;
const long long mod = 1e9+7;
const long double pi = acos(-1);
const int base = 300;
ll k, t;
ll a[N], ans, m, n, b[N], tong, d[N], c[N], lab[N], cnt, h[N], P[N][20];
vector<pll> val[N];
vector<ll> adj[N], res;
string s[N];
ll pw(ll k, ll n)
{
    ll total = 1;
    for(; n; n >>= 1)
    {
        if(n & 1)total = total * k % mod;
        k = k * k % mod;
    }
    return total;
}
template<typename T>
void read(T&x)
{
    bool Neg=false;
    char c;
    for(c= getchar();c<'0'||c>'9';c=getchar())
        if(c=='-') Neg =!Neg;
    x = c-'0';
    for (c=getchar();c>='0'&&c<='9';c=getchar())
        x=x*10+c-'0';
    if(Neg&&x>0) x=-x;
}

bool cmp(ll &x, ll &y)
{
    return a[x] > a[y];
}
void dfs(ll u, ll p)
{
    cout << u << " ";
    sort(adj[u].begin(), adj[u].end());
    for(ll v : adj[u])
    {
        if(v == p)continue;
        dfs(v, u);
        cout << u <<" ";
    }
}
bool ok(ll x, ll y)
{
    return 0 <= x && x < n && 0 <= y && y < m;
}
void sol()
{
    cin >> n >> m;
    for(int i = 0; i < n; i ++)cin >> s[i];
    fill_n(d, n*m+1, mod);
    d[0] = 0;
    priority_queue< pll, vector<pll>, greater<pll> > pq;
    pq.push({0, 0});
    while(!pq.empty())
    {
        pll u = pq.top();
        pq.pop();
        if(u.fi != d[u.se])continue;
        ll x = u.se / m, y = u.se % m;
        for(int dx = -1; dx <= 1; dx ++)
        {
            for(int dy = -1; dy <= 1; dy ++)
            {
                if(abs(dx) + abs(dy) == 2)continue;
                ll l = x + dx, r = y + dy;
                if(ok(l, r) && d[l*m+r] > u.fi && s[l][r] == '.')
                {
                    d[l*m+r] = u.fi;
                    pq.push({d[l*m+r], l*m+r});
                }
            }
        }
        for(int dx = -2; dx <= 2; dx ++)
        {
            for(int dy = -2; dy <= 2; dy ++)
            {
                if(abs(dx) + abs(dy) == 4)continue;
                ll l = x + dx, r = y + dy;
                if(ok(l, r) && d[l*m+r] > u.fi + 1)
                {
                    d[l*m+r] = u.fi + 1;
                    pq.push({d[l*m+r], l*m+r});
                }
            }
        }
    }
    cout << d[n*m-1];
}
int main()
{
    cin.tie(0);
    cout.tie(0);
    ios_base::sync_with_stdio(0);
    #define task "testss"
    if(fopen(task".inp", "r"))
    {
        freopen(task".inp", "r", stdin);
        freopen(task".out", "w", stdout);
    }
    int ntest = 1;
    while(ntest -- > 0)
    sol();
}

