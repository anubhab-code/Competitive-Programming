#include <iostream>
using namespace std;

int main() {
    int t;
	cin>>t;
	for(int i=0;i<t;i++) {
		string a;
		cin>>a;
		a[a.length() - 1] = a[0];
		cout<<a<<endl;
	}
	return 0;
}
