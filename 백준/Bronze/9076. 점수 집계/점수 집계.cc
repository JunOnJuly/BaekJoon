#include <iostream>
//
#include <array>
//
#include <algorithm>

using namespace std;


int main(void){
	int T;
	cin >> T;

	for (int _ = 0; _ < T; _++) {
		array<int, 5> score_arr{};

		for (int i = 0; i < 5; i++) {
			cin >> score_arr[i];
		}

		sort(score_arr.begin(), score_arr.end());

		if (score_arr[3] - score_arr[1] >= 4) cout << "KIN" << "\n";
		else {
			cout << score_arr[1] + score_arr[2] + score_arr[3] << "\n";
		}
	}
}