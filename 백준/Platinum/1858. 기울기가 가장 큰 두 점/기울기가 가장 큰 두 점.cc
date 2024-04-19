#include <iostream>
#include <array>
#include <vector>
#include <algorithm>
#include <cmath>
#include <limits>
#include <set>

using namespace std;

// 정렬 함수
bool sort_idx(array<int, 3>& arr_1, array<int, 3>& arr_2) {
	// x 오름차순
	return arr_1[0] < arr_2[0];
}

int main(void) {
	// 입력
	int N;
	cin >> N;
	// 좌표 정보 벡터, { { 좌표, 번호 }, 활성화 }
	vector<array<int, 3>> idxs;
	for (int i = 0; i < N; i++) {
		array<int, 3> temp_arr;
		cin >> temp_arr[0] >> temp_arr[1];
		temp_arr[2] = i + 1;
		idxs.push_back(temp_arr);
	}
	// x 오름차순, y 오름차순으로 정렬
	sort(idxs.begin(), idxs.end(), sort_idx);
	// 최대 기울기, 해당 번호
	float max_incline = 0;
	int max_A, max_B, max_i;
	// x 좌표가 인접한 좌표끼리 기울기 계산
	for (int i = 0; i < N - 1; i++) {
		float incline = static_cast<float>(idxs[i + 1][1] - idxs[i][1]) / static_cast<float>(idxs[i + 1][0] - idxs[i][0]);
		// 기울기의 절댓값이 최대 기울기의 절댓값보다 크면
		if (abs(incline) > abs(max_incline)) {
			// 기울기 최댓값 최신화
			max_incline = incline;
			// 번호, 인덱스 최신화
			max_A = min(idxs[i + 1][2], idxs[i][2]);
			max_B = max(idxs[i + 1][2], idxs[i][2]);
			max_i = i + 1;
		}
		// 기울기의 절댓값이 최대 기울기의 절댓값과 같으면
		if (abs(incline) == abs(max_incline)){
			// 값이 같고 연속되는 인덱스이면
			if (incline == max_incline and max_i == i) {
				// max_A, max_B 후보, 중복 제거
				set<int> candid_set = { max_A, max_B, idxs[i][2], idxs[i + 1][2] };
				// 벡터로 치환
				vector<int> candid_vec(candid_set.begin(), candid_set.end());
				// 정렬
				sort(candid_vec.begin(), candid_vec.end());
				// 가장 작은 두 값 할당
				max_A = candid_vec[0];
				max_B = candid_vec[1];
			}
			// 절댓값이 같거나 값이 같은데 연속되지 않는 경우
			else {
				// x 축 기준으로 앞에 있는 점이 max_A 보다 번호가 작거나
				// x 축 기준으로 뒤에 있는 점이 max_A 보다 번호가 작거나
				// x 축 기준으로 앞에 있는 점이 max_A 와 같고 뒤에 있는 점이 max_B 보다 작거나
				// x 축 기준으로 뒤에 있는 점이 max_A 와 같고 앞에 있는 점이 max_B 보다 작으면
				if (idxs[i][2] < max_A or
					idxs[i + 1][2] < max_A or
					(idxs[i][2] == max_A and idxs[i + 1][2] < max_B) or
					(idxs[i + 1][2] == max_A and idxs[i][2] < max_B)) {
					// 작은 값은 max_A
					max_A = min(idxs[i + 1][2], idxs[i][2]);
;					// 큰 값은 max_B
					max_B = max(idxs[i + 1][2], idxs[i][2]);
				}
			}
		}
	}

	cout << max_A << " " << max_B;
}