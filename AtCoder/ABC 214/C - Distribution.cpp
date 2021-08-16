#include <bits/stdc++.h>   
using namespace std;

void solve(){
    int n;
    cin>>n;
    vector<int> a(n), b(n), ans(n);
    for (int i = 0; i < n; i++)
        cin>>a[i];
    int m = INT_MAX, p;
    for (int i = 0; i < n; i++)
    {   
        cin>>b[i];
        if(b[i] < m) {
            m = b[i];
            p = i;
        }
    }
    int q;
    ans[p] = b[p];
    for (int x = 1; x < n; x++)
    {
        p = (p+1) % n;
        q = p - 1 < 0 ? n - 1 : p - 1;
        
        ans[p] = min(b[p] , ans[q] + a[q]);
    }
    for(auto y : ans)
    {
        cout<<y<<endl;
    }
}
int main()
{
    int t = 1;
    while(t--) {
        solve();
    }
    return 0;
}