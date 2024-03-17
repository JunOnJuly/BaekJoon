#include <iostream>
//
#include <array>
//
#include <algorithm>

using namespace std;

int main(void){
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	
	// 입력
	int N;
	cin >> N;

	cout << N * (N - 1);
}	