#include<bits/stdc++.h>
using namespace std;
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
using namespace __gnu_pbds;
#define ll                 long long int
#define mod                1000000007
#define modulo             998244353
#define f                  first
#define s                  second
#define pb                 push_back
#define popb               pop_back
#define  to_low(s)         transform(s.begin(), s.end(), s.begin(), ::tolower);//convert string to lowercase
#define  to_up(s)          transform(s.begin(), s.end(), s.begin(), ::toupper);//convert string to uppercase
#define inf                (ll)(1e18)
#define rep(i,a,b)         for(int i=a;i<b;i++)
#define pll                pair<ll,ll>
#define ppl                pair<ll,pair<ll,ll>>
#define mem1(a)            memset(a,-1,sizeof(a))
#define mem0(a)            memset(a,0,sizeof(a))
#define maxHeap(T)         priority_queue <T>
#define minHeap(T)         priority_queue <T, vector<T>, greater<T>> 
#define fast               ios_base::sync_with_stdio(0); cin.tie(0);cout.tie(0);
ll sieve[1000009];
const int N = 1e3 + 5;
int n;
pair<int,int> a[N];
void prime()
{
  int N=1000005;
        
  //step1 
  for(int i=2;i<=N;i++){
    sieve[i]=1;
  }
  sieve[0]=sieve[1]=0;
 
  //step2 : 
  for(int i=2;i*i<=N;i++)
  {
    if(sieve[i]==1)
    {
      for(int j=i*i; j<N;j+=i)     
      {
        sieve[j]=0;
      }
    }
  }
}
map<pair<int,int>, int>res;
map<pair<int,int>, bool>mp;

void solving(int h, int f) {
    if(h == f){
        res[{h, f}] = h;
        return;
    }
    for (int i = h; i < f+1; i++) {
        if(i == f){
            if(!(mp[{h, i - 1}]))
                continue;
            if(mp[{h, i - 1}]){
                res[{h, f}] = i;
                solving(h, i - 1);
                break;
            }
        }
        else if (i == h) {
            if (!(mp[{i + 1, f}]))
                continue;
            if (mp[{i + 1, f}]) {
                res[{h, f}] = i;
                solving(i + 1, f);
                break;
            }
        }else{
            if(!(mp[{h, i - 1}] && mp[{i + 1, f}]))
                continue;
            if( mp[{i + 1, f}] && mp[{h, i - 1}]){
                res[{h, f}] = i;
                solving(h, i - 1);
                solving(i + 1, f);
                break;
            }
        }
    }
}

void solving2() {
    cin >> n;
    mp.clear();
    res.clear();
    int h = 1, f = n;
    for(int i = 0; i < n; i++){
        cin >> a[i].f >> a[i].s;
        mp[{a[i].f, a[i].s}] = true;
    }
    solving(h, f);
    for(auto x : mp){
        if(res[x.f])
            cout << x.f.f << " " << x.f.s << " " << res[x.f] << endl;
    }
    cout << endl;
}
 
int main()
{
    fast;
    int t=1;
    cin>>t;
    prime();
    for(int i=1;i<=t;i++)
    {  
     solving2();
 
    }
   
    return 0;
}