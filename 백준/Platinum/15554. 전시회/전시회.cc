#include <iostream>
#include <array>
#include <vector>
#include <algorithm>
#include <limits>

using namespace std;

// 정렬 함수, 1순위 : 무게 , 2순위 : 가치
bool sort_prefix(array<long long int, 2>& arr_1, array<long long int, 2>& arr_2) {
	if (arr_1[0] < arr_2[0]) return true;
	else if (arr_1[0] == arr_2[0] and arr_1[1] < arr_2[1]) return true;
	else return false;
}

int main(void) {
	/*
	
	미술품이 크기별로 정렬이 되어 있을 때

	PrefixSum : 가치의 누적합 어레이
	i : 크기가 최대인 인덱스
	j : 크기가 최소인 인덱스
	
	S - (Amax - Amin)
	= PrefixSum[i] - PrefixSum[j - 1] - ( A[i] - A[j] )
	= ( PrefixSum[i] - A[i] ) - ( PrefixSum[j - 1] - A[j] )
	
	i식 - j식 이 최대가 될 가능성은 i식이 증가하고 있을 경우, j식이 감소하고 있을 경우 모두 갖고 있으므로 두 경우 모두 체크


	*/
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	// 입력
	int N;
	cin >> N;

	array<array<long long int, 2>, 500001> art_arr{};
	for (int i = 1; i <= N; i++) {
		cin >> art_arr[i][0] >> art_arr[i][1];
	}

	// 크기별로 정렬
	sort(art_arr.begin() + 1, art_arr.begin() + N + 1, sort_prefix);

	// 누적합 리스트로 치환
	for (int i = 1; i <= N; i++) {
		art_arr[i][1] += art_arr[i - 1][1];
	}

	//// 이전 i 식의 값, 이전 j 식의 값, j 식의 최솟값 구하기
	// 이전 i 식의 값
	long long int before_i = numeric_limits<long long int>::min();
	// 이전 j 식의 값
	long long int before_j = numeric_limits<long long int>::max();
	// j 식의 최솟값
	long long int min_j = numeric_limits<long long int>::max();
	// 전체 식의 최댓값
	long long int max_all{};
	// 순회
	for (int i = 1, j = 1; i < N+1; i++, j++) {
		// 후보값
		long long int candid_val_i = art_arr[i][1] - art_arr[i][0];
		long long int candid_val_j = art_arr[j - 1][1] - art_arr[j][0];

		// i 식이 증가중이면
		if (candid_val_i > before_i) {
			// 최신화
			min_j = min(candid_val_j, min_j);
			max_all = max(max_all, candid_val_i - min_j);
		}
		// j 식이 감소중이면
		else if (candid_val_j < before_j) {
			// j 가 i 보다 크면 안되므로 현재 인덱스의 전체 식 값과 비교
			max_all = max(max_all, candid_val_i - min_j);
		}
	}

	cout << max_all;

	return 0;
}