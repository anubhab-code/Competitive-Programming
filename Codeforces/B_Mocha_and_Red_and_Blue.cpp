#include <bits/stdc++.h>
using namespace std;

int main() {
	int t;
	cin>>t;
	while(t){
		int n;
		cin>>n;
		string s;
		cin>>s;
		int i,c=0;
		if(n==1 && s[0]=='?'){
		    s[0]='B';
		}
		for(i=0;i<n;i++){
			if(s[i]=='?' && (s[i+1]=='R' || s[i+1]=='B' || s[i-1]=='R' || s[i-1]=='B'))
			{
				if(s[i+1]=='R' ||s[i-1]=='R'){
				    s[i]='B';
				}
				else{
				    s[i]='R';
				}
			}
			else if(s[i]=='?'){
			    c++;
				if(s[i+1]=='R' || s[i+1]=='B' || s[i-1]=='R' || s[i-1]=='B'){
				
				}
			}
		}
		for(i=n-1;i>=0;i--){
			if(s[i]=='?' && (s[i+1]=='R' || s[i+1]=='B' ))
			{
				if(s[i+1]=='R' ||s[i-1]=='R'){
				    s[i]='B';
				}
				else{
				    s[i]='R';
				}
			}
		}
		if(c==n){
			for(i=0;i<n;i++){
				if(i%2==0){
				    s[i]='B';
				}
				else{
				    s[i]='R';
				}
			}
		}
		cout<<s<<endl;
		t--;
	}
	return 0;
}