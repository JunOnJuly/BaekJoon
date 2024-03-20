#include <iostream>
//
#include <string>
//
#include <algorithm>

using namespace std;


int main(void){
	string num;
	cin >> num;

	sort(num.begin(), num.end(), greater<char>());
	cout << num;
}