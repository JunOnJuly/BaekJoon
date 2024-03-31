#include <iostream>
#include <array>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;

// x 를 기준으로 정렬하기 위한 함수
bool sort_by_x(array<long long int, 2>& arr_1, array<long long int, 2>& arr_2) {
	return arr_1[1] < arr_2[1];
}

int main(void) {
	// 줄
	array<array<long long int, 2>, 1000001> line_arr{};
	// 입력
	int N;
	cin >> N;
	for (int i = 0; i < N; i++) {
		array<long long int, 2> temp_arr;
		cin >> temp_arr[0] >> temp_arr[1];

		// 남자면 성별 인식 수를 -1로 변환
		if (temp_arr[0] == 0) temp_arr[0] = -1;

		line_arr[i + 1] = temp_arr;
	}

	// x 좌표를 기준으로 정렬
	sort(line_arr.begin() + 1, line_arr.begin() + N + 1, sort_by_x);
	
	// 누적합 맵
	map<int, vector<int>> prefix_map;
	prefix_map.insert(pair<int, vector<int>>(0, { 0 }));
	// 남여 인식수를 누적합
	// 뒤 누적합 - 앞 누적합 = 0 이면 해당 구간은 남여 수 일치
	for (int i = 0; i < N; i++) {
		line_arr[i + 1][0] += line_arr[i][0];
		// 맵에 기록
		// 이미 맵에 존재하면
		if (prefix_map.find(line_arr[i + 1][0]) != prefix_map.end()) {
			prefix_map[line_arr[i + 1][0]].push_back(i + 1);
		}
		// 존재하지 않으면
		else {
			prefix_map.insert(pair<int, vector<int>>(line_arr[i + 1][0], { i + 1 }));
		}
	}

	// 최대 길이
	long long int max_len{};
	// 맵을 순회
	for (auto iter = prefix_map.begin(); iter != prefix_map.end(); iter++) {
		// 맵에 속한 벡터
		auto iter_vec = iter->second;
		// 맵에 인덱스가 두 개 이상이면
		if (iter_vec.size() >= 2) {
			// 맨 뒤와 맨 처음의 차이와 최댓값 비교
			max_len = max(max_len, line_arr[iter_vec.back()][1] - line_arr[iter_vec.front()+1][1]);
		}
	}

	cout << max_len;
}