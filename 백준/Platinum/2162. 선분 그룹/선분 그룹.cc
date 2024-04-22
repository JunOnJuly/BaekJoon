#include <iostream>
#include <array>
#include <vector>
#include <algorithm>
#include <cmath>
#include <limits>
#include <map>
#include <deque>

using namespace std;

// 점을 저장할 구조체
struct Point {
	// 좌표
	int x;
	int y;
};
// 직선 데이터를 저장할 구조체
struct Line {
	// 속한 점들
	Point point_1;
	Point point_2;
	// 속한 그룹
	int group;
	// 순회 여부
	bool visited = false;
};

// ccw
long long int ccw(Point point_1, Point point_2, Point point_3) {
	// 포인트 어레이
	array<Point, 4> points = { point_1, point_2, point_3, point_1 };
	// ccw 값
	long long int ccw_sum = 0;
	// 계산
	for (int i = 0; i < 3; i++) {
		ccw_sum += points[i].x * points[i + 1].y;
		ccw_sum -= points[i].y * points[i + 1].x;
	}

	return ccw_sum;
}

// 교차하는지 판단
bool is_cross(Line line_1, Line line_2) {
	// ccw
	long long int ccw_1 = ccw(line_1.point_1, line_1.point_2, line_2.point_1);
	long long int ccw_2 = ccw(line_1.point_1, line_1.point_2, line_2.point_2);
	long long int ccw_3 = ccw(line_2.point_1, line_2.point_2, line_1.point_1);
	long long int ccw_4 = ccw(line_2.point_1, line_2.point_2, line_1.point_2);
	// 곱한 값들
	long long int result_1 = ccw_1 * ccw_2;
	long long int result_2 = ccw_3 * ccw_4;
	// 값의 곱이 모두 음수면 완벽한 교차
	if (result_1 < 0 and result_2 < 0) return true;
	// 값의 곱이 모두 양수면 교차하지 않음
	else if (result_1 > 0 and result_2 > 0) return false;
	// 값의 곱의 하나가 0 이고 나머지가 음수이면 교차
	else if ((result_1 == 0 and result_2 < 0) or (result_1 < 0 and result_2 == 0)) return true;
	// 값의 곱의 하나가 0 이고 나머지가 양수이면 교차하지 않음
	else if ((result_1 == 0 and result_2 > 0) or (result_1 > 0 and result_2 == 0)) return false;
	// 값의 곱의 하나가 양수이고 나머지가 음수이면 교차하지 않음
	else if ((result_1 > 0 and result_2 < 0) or (result_1 < 0 and result_2 > 0)) return false;
	// 나머지 ( 값의 곱이 모두 0 )
	else {
		// 두 선분이 같은 직선상에 있고 만나지 않을 때
		if ((((line_1.point_1.x > line_2.point_1.x and line_1.point_2.x > line_2.point_1.x) and
			(line_1.point_1.x > line_2.point_2.x and line_1.point_2.x > line_2.point_2.x)) or
			((line_1.point_1.y > line_2.point_1.y and line_1.point_2.y > line_2.point_1.y) and
				(line_1.point_1.y > line_2.point_2.y and line_1.point_2.y > line_2.point_2.y))) or

			(((line_2.point_1.x > line_1.point_1.x and line_2.point_2.x > line_1.point_1.x) and
				(line_2.point_1.x > line_1.point_2.x and line_2.point_2.x > line_1.point_2.x)) or
				((line_2.point_1.y > line_1.point_1.y and line_2.point_2.y > line_1.point_1.y) and
					(line_2.point_1.y > line_1.point_2.y and line_2.point_2.y > line_1.point_2.y)))) return false;
		// 나머지
		else return true;
	}
}

// 파인드
int Find(vector<Line>& lines, int& i) {
	// 자신의 그룹이 자신이면
	if (lines[i].group == i) return i;
	// 자신의 그룹이 자신이 아니면
	else {
		lines[i].group = Find(lines, lines[i].group);
	}
	return lines[i].group;
}

// 유니온
void Union(vector<Line>& lines, int& i, int& j) {
	// 두 선분의 그룹
	int group_i = Find(lines, i);
	int group_j = Find(lines, j);
	// 두 선분의 그룹이 다르면
	if (group_i != group_j) {
		// j 의 그룹을 i 의 그룹으로 변경
		lines[j].group = group_i;
		// 그룹을 변경했으면 false
	}
}

int main(void) {
	// 입력
	int N;
	cin >> N;
	// 직선을 저장할 벡터
	vector<Line> lines;
	for (int i = 0; i < N; i++) {
		Line line;
		cin >> line.point_1.x >> line.point_1.y >> line.point_2.x >> line.point_2.y;
		// 우선 자신은 자신의 그룹
		line.group = i;
		lines.push_back(line);
	}
	deque<int> dq = { 0 };
	lines[0].visited = true;
	// 직선 순회
	while (true) {
		// 큐가 비었으면
		if (dq.empty()) {
			// 직선 선택
			for (int i = 0; i < N; i++) {
				// 방문하지 않은 직선이면
				if (!lines[i].visited) {
					// 큐에 삽입
					dq.push_back(i);
					// 방문 체크
					lines[i].visited = true;
					break;
				}
			}
			// 선택된 직선이 없으면 끝
			if (dq.empty()) break;
		}
		// 교차판단할 직선
		int line_1 = dq.front();
		dq.pop_front();
		// 선택된 직선과 다른 직선들 교차판단
		for (int i = 0; i < N; i++) {
			// 교차판단할 나머지 직선
			int line_2 = i;
			// 같은 직선이면 패스
			if (i == line_1) continue;
			// 이미 방문한 직선이면 패스
			if (lines[i].visited) continue;
			// 교차하면
			if (is_cross(lines[line_1], lines[line_2])) {
				// 방문 체크
				lines[line_2].visited = true;
				// 큐에 삽입
				dq.push_back(line_2);
				// 유니온
				Union(lines, line_1, line_2);
			}
		}
	}
	// 속한 그룹을 저장할 맵
	map<int, int> groups;
	// 직선을 순회
	for (int i = 0; i < N; i++) {
		// 그룹을 검색
		int group = Find(lines, i);
		// 이미 존재하는 그룹이면
		if (groups.find(group) != groups.end()) {
			// 그룹에 + 1
			groups[group] += 1;
		}
		// 존재하지 않으면
		else {
			// 그룹 추가
			groups.insert({ group, 1 });
		}
	}
	// 가장 크기가 큰 그룹에 속한 선분 수
	int max_lines = 0;
	for (auto pr : groups) {
		// 최신화
		max_lines = max(max_lines, pr.second);
	}

	cout << groups.size() << "\n" << max_lines;
}