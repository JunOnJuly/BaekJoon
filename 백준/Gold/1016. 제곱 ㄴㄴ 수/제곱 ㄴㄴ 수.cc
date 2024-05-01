
#include <iostream>
#include <array>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

// 소수를 찾는 함수
vector<long long int> search_unique(long long int& max) {
	// 소수 목록
	vector<long long int> uniques;
	// 수 체크를 위한 벡터
	vector<bool> nums(max, true);
	// 순회
	for (long long int i = 2; i <= max; i++) {
		// i 가 체크되어 있지 않으면
		// k 가 소수이면 nk 는 소수가 아님이 자명하므로
		if (nums[i - 1]) {
			uniques.push_back(i);
			for (long long int j = i; j <= max; j += i) {
				// j 가 체크되어 있지 않으면
				if (nums[j - 1]) nums[j - 1] = false;
			}
		}
	}

	return uniques;
}

// 벡터의 제곱수들을 출력하는 함수
vector<long long int> squares(vector<long long int>& vec) {
	// 순회하며 제곱
	for (long long int i = 0; i < vec.size(); i++) {
		vec[i] = pow(vec[i], 2);
	}

	return vec;
}

// MAX 이하의 소수의 제곱수를 찾는 함수
vector<long long int> search_under_square(long long int& max) {
	// 소수의 제곱수
	vector<long long int> square_uniques;
	// max 의 제곱근 (long long int)
	long long int sqrt_max = static_cast<long long int>(sqrt(max));
	// max 이하의 소수
	vector<long long int> uniques = search_unique(sqrt_max);
	// 소수의 제곱 벡터

	return squares(uniques);
}

// 특정 수들 체로 특정 범위의 수들을 걸러내는 함수
long long int filter_nums(vector<long long int>& vec, long long int& MIN, long long int& MAX) {
	// 걸러낼 범위의 수들
	vector<bool> nums(MAX - MIN + 1, true);
	// 걸러내기
	for (auto num : vec) {
		// min 보다 큰 최소 배수
		long long int min_num = MIN%num == 0 ? MIN : num * (MIN / num) + num;
		// max 보다 작은 최대 배수
		long long int max_num = MAX%num == 0 ? MAX : num * (MAX / num);
		// 배수 체크
		for (long long int i = min_num; i <= max_num; i += num) nums[i - MIN] = false;
	}

	return count(nums.begin(), nums.end(), true);
}

int main(void) {
	// 입력
	long long int MIN, MAX;
	cin >> MIN >> MAX;
	// MAX 이하의 (소수의 제곱수)들
	auto square_uniques = search_under_square(MAX);
	// 걸러내기
	cout << filter_nums(square_uniques, MIN, MAX);
}