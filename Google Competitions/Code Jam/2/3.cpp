# include<iostream> 
#include <bits/stdc++.h> 
#include <unordered_set>
using namespace std;

int main(){
int T, q = 0;
cin >>T;

unordered_set <int> T;
int k=0;
for (k=0;k<10**4;k++){
	T.insert(k*k);
}

while (q<t){
	q++;
	int n;
	cin >>n;
	int A[n], i=0;
	for (i=0; i<n; i++){
		cin >> A[i];
	}
	
	int PS[n+1];
	PS[0] = 0;
	int s = 0
	
	for (i=0;i<n;i++){
		s += A[i];
		PS[i+1] = s;
	}
	
	int j, count = 0;
	
	for (i=0;i<n+1;i++){
		for (j=0;j<i;j++){
			k = PS[i] - PS[j];
			if (T.find(k) != T.end()){
				count+=1
			}
		}
	}
	
	cout << "Case #" << q <<": " << count;
}
return 0;
}

