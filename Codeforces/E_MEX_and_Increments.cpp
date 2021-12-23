#include<bits/stdc++.h>
using namespace std;
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
using namespace __gnu_pbds;
#define ll                 long long int
#define mod                1000000007
#define modulo             998244353
#define pie                3.141592653589793
#define popcount           __builtin_popcount     //used to count number of set bits in a integer
#define llpopcount         __builtin_popcountll   
#define parity             __builtin_parity // returns true(1) if number has odd parity i.e odd no of set bits
#define llparity           __builtin_parityll 
#define leadzero           __builtin_clz  //returns number of leading zeros of a 32 bit int 
#define llleadzero         __builtin_clzll // returns number of leading zero of a 64 bit int 
#define trailzero          __builtin_ctz  // returns number of trailing zero 
#define lltrailzero        __builtin_ctzll 
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
#define deb(x)             cout<<#x<<" "<<x<<"\n"
#define uid(l,r)           uniform_int_distribution<int>(l,r); // to use auto temp= uid(l,r). int x= temp(rng); to generate from [L,R]
template<typename T,typename T1>T amax(T &a,T1 b){if(b>a)a=b;return a;} // only use in equations like sum=max(sum,x)  its equivalent ot amax(sum,x) => sums is changed automatically
template<typename T,typename T1>T amin(T &a,T1 b){if(b<a)a=b;return a;}
template<typename T> using pbds =tree<T,null_type,less<T>,rb_tree_tag,tree_order_statistics_node_update>; // *s.find_by_order(x)=> xth element on 0 based indexing  , s.order_of_key(x) => no of elements strictly smaller
mt19937 rng(chrono::steady_clock::now().time_since_epoch().count()); 
void read_input()
{
  #ifndef ONLINE_JUDGE
  freopen("inputA.txt","r",stdin);
  freopen("outputA.txt","w",stdout);
  #endif
}
ll sieve[1000009];
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

ll solving() {
    ll n;
    string s;
    cin>>n;
    map<ll,ll> mp;
    vector<ll> a(n),hehe;
    
    for(ll i=0;i<n;i++){
        cin>>a[i];
        mp[a[i]]++;
    }
    sort(a.begin(),a.end());
 
    ll ans=0;
    ll last=-1;
    int flag=0;
   
   for(ll i=0;i<=n;i++){
        if(!(last<i-1 || flag)){
            cout<<ans+mp[i]<<' ';
        }
        else{
            flag=1;
            cout<<-1<<' ';
        }
        if((mp[i])){
            last=i;
            if(mp[i]<=1) {
                continue;
            }
            else if(mp[i]>1) {
                mp[i]--;
                hehe.pb(i); 
            }
        }
        else if(hehe.size()){
            last=i;
            ll bal= hehe.back();
            ll t2=-(bal-i);
            ans+=t2;
            mp[bal]--;
            if(mp[bal]!=0){
                continue;
            } 
            else{
               hehe.popb(); 
            }
            
      } 
   }
 
   cout<<endl;
}

 
int main()
{
    fast;
    int t=1;
    cin>>t;
    prime();
    // read_input();
    for(int i=1;i<=t;i++)
    {  
    //cout<<"Case #"<<i<<": ";
     solving();
 
    }
   
    return 0;
}