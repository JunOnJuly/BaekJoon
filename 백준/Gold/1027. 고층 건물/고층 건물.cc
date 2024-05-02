
#include <iostream>
#include <array>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

// 점을 기록할 구조체
struct Point {
	// 좌표
	long long int x;
	long long int y;
};

// 선분을 기록할 구조체
struct Line {
	// 양 끝점
	Point pt_1;
	Point pt_2;
};

// ccw
int ccw(Line& sight, Point& building_top) {
	// 외적을 위한 벡터
	vector<Point> ccw_vec = { sight.pt_1, sight.pt_2, building_top, sight.pt_1 };
	// 외적 값
	long long int ccw_value = 0;
	// 계산
	for (int i = 0; i < 3; i++) {
		ccw_value += ccw_vec[i].x * ccw_vec[i + 1].y;
		ccw_value -= ccw_vec[i + 1].x * ccw_vec[i].y;
	}
	// 음수면 시계방향(-1), 양수면 반시계방향(1), 0 이면 같은 직선상(0) 
	return ccw_value > 0 ? 1 : ccw_value == 0 ? 0 : -1;
}

// 현재 건물에서 보이는 건물의 수를 세는 함수
int count_build(int& now_build, int& next_build, vector<long long int> buildings, bool& dir, int& build_num, int& N) {
	// 사선을 이을 다음 건물이 인덱스를 벗어나면
	if (next_build < 0 or next_build >= N) return build_num;
	// 현재 위치
	Point now_pt = Point{ now_build, buildings[now_build] };
	// 시선을 이을 다음 위치
	Point next_pt = Point{ next_build, buildings[next_build] };
	// 시선 선분
	Line sight = { now_pt , next_pt };
	// 타겟 인덱스
	int target_build = next_build;
	// 순회
	while (true) {
		// 방향을 비교할 포인트
		Point target_pt;
		// 왼쪽 방향이면
		if (!dir) {
			// 방향을 비교할 인덱스, 포인트
			target_build -= 1;
			// 방향을 비교할 인덱스가 범위를 넘으면 리턴
			if (target_build < 0) return build_num;
		}
		// 오른쪽 방향이면
		else {
			// 방향을 비교할 인덱스, 포인트
			target_build += 1;
			// 방향을 비교할 인덱스가 범위를 넘으면 리턴
			if (target_build >= N) return build_num;
		}
		// 방향을 비교할 포인트
		target_pt = { target_build, buildings[target_build] };
		// ccw 방향
		int ccw_dir = ccw(sight, target_pt);
		// 왼쪽 방향이면
		if (!dir) {
			// 시계 방향이면
			if (ccw_dir == -1) {
				// 보이는 건물 + 1
				build_num += 1;
				build_num = count_build(now_build, target_build, buildings, dir, build_num, N);
				break;
			}
		}
		// 오른쪽 방향이면
		else {
			// 반시계 방향이면
			if (ccw_dir == 1) {
				// 보이는 건물 + 1
				build_num += 1;
				build_num = count_build(now_build, target_build, buildings, dir, build_num, N);
				break;
			}
		}
	}
	return build_num;
}

int main(void) {
	// 입력
	int N;
	cin >> N;
	// 건물 높이를 기록할 벡터
	vector<long long int> buildings;
	for (int i = 0; i < N; i++) {
		long long int height;
		cin >> height;
		buildings.push_back(height);
	}
	// 보이는 건물의 최댓값
	int max_build = 0;
	// 건물 위치 순회
	for (int i = 0; i < N; i++) {
		// 현재 건물
		int now_build = i;
		// 현재 건물에서 보이는 건물의 수 ( 바로 옆 건물들은 그냥 보임 )
		int watchable_build = i == 0 and i == N - 1 ? 0 : i == 0 or i == N - 1 ? 1 : 2;
		// 현재 건물 왼쪽 건물
		int left_build = now_build - 1;
		// 왼쪽 방향
		bool left_dir = false;
		// 현재 건물에서 왼쪽 탐색
		watchable_build = count_build(now_build, left_build, buildings, left_dir, watchable_build, N);
		// 현재 건물 오른쪽 건물
		int right_build = now_build + 1;
		// 오른쪽 방향
		bool right_dir = true;
		// 현재 건물에서 오른쪽 탐색
		watchable_build = count_build(now_build, right_build, buildings, right_dir, watchable_build, N);
		// 최댓값 최신화
		max_build = max(max_build, watchable_build);
	}

	cout << max_build;
}