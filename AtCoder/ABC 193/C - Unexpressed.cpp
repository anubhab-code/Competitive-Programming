#include <bits/stdc++.h> 
using namespace std; 
#define N 1000005 
#define MAX 1e18 
vector<long int> powers; 
set<long int> squares; 
set<long int> s; 
  
void powersPrecomputation() 
{ 
    for (long int i = 2; i < N; i++)  
    { 
        squares.insert(i * i); 
        if (squares.find(i) != squares.end()) 
                continue; 
        long int temp = i; 
        while (i * i <= MAX / temp)  
        { 
            temp *= (i * i); 
            s.insert(temp); 
        } 
    } 
    for (auto x : s) 
        powers.push_back(x); 
} 
  
long int calculateAnswer(long int L, long int R) 
{ 
    long int perfectSquares = floor(sqrtl(R)) - floor(sqrtl(L - 1)); 
    long int high = (upper_bound(powers.begin(), powers.end(), R) - powers.begin()); 
    long int low = (lower_bound(powers.begin(), powers.end(), L) - powers.begin()); 
    perfectSquares += (high - low); 
    return perfectSquares; 
} 
int main() 
{ 
    powersPrecomputation(); 
    long int L = 0; 
    long int R = 0; 
    long int n = 0;
    cin>>n;
    L = 1; 
    R = n; 
    cout << (n-calculateAnswer(L, R)+1) << endl; 
    return 0; 
}