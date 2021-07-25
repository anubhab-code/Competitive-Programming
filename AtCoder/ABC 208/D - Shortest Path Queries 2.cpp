#include <bits/stdc++.h>
using namespace std;
#define int long long int
 
 
int32_t main() {
	int n,m,inf=1e17;
	cin>>n>>m;
	vector<vector<int>> mat(n+1,vector<int>(n+1,inf));
	for(int i=0;i<m;i++)
	{
		int a,b,c;
		cin>>a>>b>>c;
		mat[a][b]=c;
	}
	int ans=0;
	for(int k=1;k<=n;k++)
	{
		for(int i=1;i<=n;i++)
		{
			for(int j=1;j<=n;j++)
			{
				if(i==j)
				{
					mat[i][j]=0;
				}
				else if(mat[i][j]>mat[i][k]+mat[k][j])
				{
					mat[i][j]=mat[i][k]+mat[k][j];
				}
 
				if(mat[i][j]!=inf)
				{
					ans+=mat[i][j];
				}
			}
		}
	}
	cout<<ans;
 
 
 
	return 0;
}