#include <iostream>
//
#include <array>
#include <vector>
//
#include <algorithm>

using namespace std;


int main(void){
	array<array<int, 2>, 8> scores{};
	for (int i = 0; i < 8; i++) {
		int score;
		cin >> score;

		scores[i] = { score, i + 1 };
	}

	sort(
		scores.begin(),
		scores.end(),
		[](array<int, 2> arr_1, array<int, 2> arr_2) {
			return arr_1[0] < arr_2[0];
		}
	);

	int answer_sum{};
	vector<int> answer_nums;
	for (int i = 7; i >= 3; i--) {
		answer_sum += scores[i][0];
		answer_nums.push_back(scores[i][1]);
	}
	sort(answer_nums.begin(), answer_nums.end());

	cout << answer_sum << "\n";
	for (auto num : answer_nums) {
		cout << num << " ";
	}
}