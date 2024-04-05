#include <iostream>
#include <algorithm>
#include <vector>
#include <array>
#include <limits>
#include <map>
#include <set>
#include <deque>
#include <string>

using namespace std;

int main(void) {
	int T;
	cin >> T;

	for (int i = 0; i < T; i++) {
		int N, M;
		cin >> N >> M;

		int cnt = 0;

		for (int j = N; j <= M; j++) {
			string num = to_string(j);
			for (int k = 0; k < num.size(); k++) {
				if (num[k] == '0') cnt += 1;
			}
		}
		cout << cnt << "\n";
	}
}