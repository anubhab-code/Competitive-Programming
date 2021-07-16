#include<bits/stdc++.h>
using namespace std;

int main(){
    int tt;
    cin >> tt;
    while(tt--){
        int n, cur_num = 9;
        cin >> n;
        cout << cur_num ;
        if(!(n <= 1)){
            cout << 8 ;
            n -= 2 ;
            cur_num = 9 ;
            while(n--){
                cout << cur_num ;
                if(cur_num == 9)
                    cur_num = 0;
                else
                    cur_num++;
            }
        }
        cout << "\n" ;
    }
    return 0 ;
}