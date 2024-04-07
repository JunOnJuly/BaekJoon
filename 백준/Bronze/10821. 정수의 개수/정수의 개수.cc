#include <iostream>
#include <vector>
#include <array>
#include <algorithm>
#include <string>

using namespace std;

int main(void) {
	string ipt;
	cin >> ipt;
	int cnt = 1;
	for (auto chr : ipt) {
		if (chr == ',') {
			cnt += 1;
		}
	}
	cout << cnt;
}