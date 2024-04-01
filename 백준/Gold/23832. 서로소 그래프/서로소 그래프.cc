#include <iostream>
#include <array>
#include <vector>
#include <algorithm>

using namespace std;

int main(void) {
	// 입력
	int N;
	cin >> N;

	// 수 목록
	array<bool, 50001> nums;
	nums.fill(true);
	// 소인수 목록
	array<vector<int>, 50001> factors;
	// 순회
	for (int i = 2; i < N / 2 + 1; i++) {
		// 현재 수가 true 일 때, 앞선 수의 배수가 아닐 때
		if (nums[i]) {
			// 현재 수의 배수 체크
			for (int j = 2 * i; j < N + 1; j += i) {
				nums[j] = false;
				// 소인수 목록에 넣기
				factors[j].push_back(i);
			}
		}
	}

	// 오일러 피 함수에 따라
	// pi(소수) = 소수 - 1
	// pi(소수가 아닌 수) = 소수가 아닌 수 * ( (1 - 1/소인수) 들의 곱 )
	// 간선들의 합
	long long int sum_edges = 0;
	// 순회, i = 1 인 경우는 카운트하지 않음
	for (int i = 2; i < N + 1; i++) {
		// 소수면
		if (nums[i]) sum_edges += i - 1;
		// 아니면
		else {
			int add_num = i;
			for (auto factor : factors[i]) {
				add_num *= (factor - 1);
				add_num /= factor;
			}
			sum_edges += add_num;
		}
	}

	cout << sum_edges;
}