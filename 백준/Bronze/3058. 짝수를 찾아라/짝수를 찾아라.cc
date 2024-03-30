#include <iostream>
#include <array>
#include <vector>
#include <algorithm>

using namespace std;

int main(void) {
	int T;
	cin >> T;
	for (int _ = 0; _ < T; _++) {
		int sum_even{};
		int min_even = 100;
		for (int i = 0; i < 7; i++) {
			int num;
			cin >> num;
			if (num % 2 == 0) {
				sum_even += num;
				min_even = min(min_even, num);
			}
		}
		cout << sum_even << " " << min_even<<"\n";
	}
}