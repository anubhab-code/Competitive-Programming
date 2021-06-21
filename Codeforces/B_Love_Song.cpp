#include<bits/stdc++.h>
using namespace std;
#define ll long long
 
void haha(){
    ll n,q;
    cin>>n>>q;
    int c=n+1;
    map<int,int> m[c],p[c];
    string hehe;
    cin>>hehe;
    for(int i=0;i<=n-1;i++){
        for(auto lol:m[i+1-1])
            m[i+1][lol.first]=lol.second;
        m[i+1][hehe[i+1-1]-'a']=m[i+1][hehe[i+1-1]-'a']+1;
    }
    for(int j=n-1;j>=0;j--){
        for(auto lol:p[j+1])
            p[j][lol.first]=lol.second;
        p[j][hehe[j]-'a']=j;
    }
    for(int k=0;k<q;++k){
        ll f,g;
        cin>>f>>g;
        map<int,int> dict;
        for(auto lol:m[g]){
            dict[lol.first]=lol.second-m[f-1][lol.first];
        }
        ll final=0;
        for(auto lol:dict){
            final=final+(lol.first+1)*(lol.second);
        }
        cout<<final<<endl;
    }
}
 
int main(){
    int check=1;
    while(check--){
        haha();
    }
}