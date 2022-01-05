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
const int N = 2e5 + 5;
int n;
int a[N];
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


bool solve(int x){
    int t[n+2];
    mem0(t);
    for(int i = n - 1; i >= 2; i--){
        if(a[i] + t[i] <= x-1) return false;
        int h = 0, f = a[i], mid, ans = 0;
        while (h < f+1){
            mid = (h + f)/2;
            if(!(3 * mid <= a[i] && a[i] - (3 * mid) + t[i] >= x)){
                f = mid - 1;
            }else{
                ans = mid;
                h = mid + 1;
            }
        }
        t[i - 2] = t[i-2] + (2 * ans);
        t[i - 1] = t[i-1] + ans;
        
    }
    if(!( t[1] + a[1] >= x && t[0] + a[0] >= x)) return false;
    return true;
}


void solving2() {
    cin >> n;
    for(int i = 0; i < n; i++)
        cin >> a[i];
    int mid;
    int res;
    int h = 1, f = 1e11;
    while (h < f+1){
        mid = (h + f)/2;
        if(solve(mid)){
            res = mid;
            h = mid + 1;
        }else{
            f = mid - 1;
        }
    }
    cout << res << endl;
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