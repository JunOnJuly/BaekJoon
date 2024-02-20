#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main(void)
{
	string A, B;
	cin >> A >> B;

	reverse(A.begin(), A.end());
	reverse(B.begin(), B.end());

	cout << max(stoi(A), stoi(B));
}