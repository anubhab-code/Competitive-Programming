#include<bits/stdc++.h>
using namespace std;
#define ll long long
 
bool myfunc(pair<ll,ll> a, pair<ll,ll> b){
    return b.second>a.second;
}
void haha(){
    ll n;
    cin>>n;
    vector<pair<ll,ll>> l(n);
    ll final=0;
    for(ll i=0;i<n;i++)
    {
        cin>>l[i].first>>l[i].second;
        final = 2*l[i].first + final;
    }
    sort(l.begin(),l.end(),myfunc);
    reverse(l.begin(),l.end());
    ll i=0,j=n-1;
    ll o =0;
    while(j>=i){
        ll tes=l[j].second;
        if(i==j){
            ll h=l[i].first;
            ll m=max(l[i].second-o,0ll);
            h=max(h-m,0ll);
            final-=h;
            break;
        }
        else if(tes<=o){
            o=o+l[j].first;
            final=final-l[j].first;
            j--;
        }
        else if(l[j].second>=o+l[i].first){
            o=o+l[i].first;
            l[i].first=0;
            i++;
        }
        else{
            ll m=l[j].second-o;
            o=o+m;
            o=o+l[j].first;
            l[i].first-=m;;
            final=final-l[j].first;
            j--;
        }
    }
    cout<<final<<endl;
 
}
 
int main(){
    int check=1;
    while(check--){
        haha();
    }
}