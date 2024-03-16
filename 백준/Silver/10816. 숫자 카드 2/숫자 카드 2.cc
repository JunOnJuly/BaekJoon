#include <iostream>
//
#include <map>
//
#include <algorithm>

using namespace std;

int main(void){
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	
	// 맵
	map<int, int> num_map;

	// 입력
	int N;
	cin >> N;
	for (int i = 0; i < N; i++) {
		int num;
		cin >> num;

		// 맵에 존재하면
		if (num_map.find(num) != num_map.end()) num_map[num] += 1;
		// 존재하지 않으면
		else num_map[num] = 1;
	}

	// 출력
	int M;
	cin >> M;
	for (int i = 0; i < M; i++) {
		int num;
		cin >> num;
		
		// 맵에 존재하면
		if (num_map.find(num) != num_map.end()) cout << num_map[num] << " ";
		// 존재하지 않으면
		else cout << 0 << " ";
	}
}	