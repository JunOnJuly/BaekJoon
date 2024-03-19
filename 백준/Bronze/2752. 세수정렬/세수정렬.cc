#include <iostream>
//
#include <array>
//
#include <algorithm>

using namespace std;


int main(void){
	array<int, 3> nums;
	for (int i = 0; i < 3; i++) {
		cin >> nums[i];
	}

	sort(nums.begin(), nums.end());
	for (auto num : nums) {
		cout << num << " ";
	}
}