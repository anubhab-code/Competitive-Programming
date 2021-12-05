#include <bits/stdc++.h>
using namespace std;
#define DRID cin.tie(0), cout.tie(0), cin.sync_with_stdio(0), cout.sync_with_stdio(0);
#define ll long long
#define E '\n'
#define EPS 1e-9
#define INF INT_MAX
const ll  MOD = 1e9+7  ;
const ll  N = 1e5 + 4;
 
int main() {
    DRID
    ll t;
    cin >> t;
    while (t--){
        ll n;
        cin >> n;
        int ans[n];
        int check=n-1;
        int flag=0;
        int temp;
        for (int i=0;i<n;i++){
            cin>>temp;
            if(temp!=n){
                ans[check-1]=temp;
                check--;
            }
            else{
                flag=i;
            }
        }
        if (!(flag==0||flag==n-1)){
            cout<<-1<<endl;
        }
        else{
            cout<<n<<" ";
            for(int j=0;j<=n-2;++j){
                cout<<ans[j]<<" ";
            }
            cout<<endl;
        }
    }
}