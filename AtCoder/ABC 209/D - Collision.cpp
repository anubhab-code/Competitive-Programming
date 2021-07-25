#include <bits/stdc++.h>
#define int long long
#define pb push_back
#define mp make_pair
#define all(x) x.begin() , x.end()
#define ff first
#define ss second
#define pii pair<int , int>
#define rall(x) x.rbegin() , x.rend()
#define fast ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
#define debug(a) cout << #a << " = " << a << endl;
#define files freopen("input.in", "r", stdin);freopen("input.out", "w", stdout); 
#define fff cout << "--------------------------" << endl;
using namespace std;
const int MOD = 1e9 + 7;
const int LOG = 19;
const int INF = 1e18;
const double PI = acos(-1);
const double EPS = 1e-9;
const int N = 3e5 + 5;
 
//(a / b) % p == a* (b ^ (p - 2))
 
int n, m, l = 1 , timer = 0 , tests;
vector< vector<int> >g, up;
vector< pair<int, int> >roads;
vector<int>tin, tout, deep , c;
 
void dfs(int v, int p, int cur_deep) {
	up[v][0] = p;
	deep[v] = cur_deep;
	for (int i = 1; i <= l; i++) {
		up[v][i] = up[up[v][i - 1]][i - 1];
	}
	tin[v] = timer++;
	for (int to : g[v]) {
		if (to == p) continue;
		dfs(to, v, cur_deep + 1);
	}
	tout[v] = timer++;
}
 
bool isUpper(int a, int b) {
	return tin[a] <= tin[b] && tout[a] >= tout[b];
}
 
int lca(int a, int b) {
	if (isUpper(a, b)) return a;
	if (isUpper(b, a)) return b;
	for (int i = l; i >= 0; i--) {
		if (!isUpper(up[a][i], b)) {
			a = up[a][i];
		}
	}
	return up[a][0];
}
 
int dist(int a , int b) {
	int gg = lca(a , b);
	return deep[a] + deep[b] - 2 * deep[gg];
}
 
map<int , set<int> >comp;
 
void solve() {
	cin >> n >> tests;
	while ((1 << l) < n) ++l;
	g.resize(n);
	up.resize(n);
	c.resize(n);
	tin.resize(n);
	tout.resize(n);
	roads.resize(n);
	deep.resize(n);
	for (int i = 0; i < n; i++) up[i].resize(l + 1);
	for (int i = 0; i < n - 1; i++) {
		int x , y;
		cin >> x >> y;
		x-- , y--;
		g[x].pb(y);
		g[y].pb(x);
	}
	dfs(0 , 0 , 0);
	for (; tests > 0; tests--) {
		int x , y;
		cin >> x >> y;
		x-- , y--;
		int gg = dist(x , y);
		if (gg % 2 == 0) cout << "Town" << endl;
		else cout << "Road" << endl;
	}
}
 
signed main() { 
  fast
  int t = 1;
  while (t--) solve();
  return 0; 
}