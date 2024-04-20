#include <iostream>
#include <array>
#include <vector>
#include <algorithm>
#include <cmath>
#include <limits>
#include <set>

using namespace std;

// 점 구조체
struct Point {
	// x y 좌표
	long long int x;
	long long int y;
	// 기준 점
	array<long long int, 2> origin_point;
};

// ccw
long long int ccw(Point& point_1, Point& point_2, Point& point_3) {
	// 임시 어레이
	array<Point, 4> point_arr = { point_1, point_2, point_3, point_1 };
	// 계산
	long long int ccw_sum = 0;
	for (int i = 0; i < 3; i++) {
		ccw_sum += point_arr[i].x * point_arr[i + 1].y;
		ccw_sum -= point_arr[i].y * point_arr[i + 1].x;
	}
	return ccw_sum;
}

// x 기준 오름차순으로 정렬
bool sort_point(Point& point_1, Point& point_2) {
	// 우선 x 기준
	if (point_1.x < point_2.x) return true;
	// x 가 같으면 y 기준
	else if (point_1.x == point_2.x and point_1.y < point_2.y) return true;
	// 나머지
	else return false;
}

// 시계 방향으로 정렬
bool sort_clock_wise(Point& point_1, Point& point_2) {
	// 기준 점
	Point origin_point;
	origin_point.x = point_1.origin_point[0];
	origin_point.y = point_1.origin_point[1];
	// ccw
	long long int ccw_points = ccw(origin_point, point_1, point_2);
	// origin_point / point_1, origin_point / point_2 거리 비교
	long long int dist_o1 = pow((origin_point.y - point_1.y), 2) + pow((origin_point.x - point_1.x), 2);
	long long int dist_o2 = pow((origin_point.y - point_2.y), 2) + pow((origin_point.x - point_2.x), 2);
	// 음수면 시계방향
	if (ccw_points < 0) return true;
	// 0 이면 직선방향, origin_point 와 가까우면 앞으로
	else if (ccw_points == 0 and dist_o1 < dist_o2) return true;
	// 양수면 반시계
	else return false;
}

// 그라함 스캔
vector<Point> graham_scan(vector<Point>& points) {
	// 스택
	vector<Point> stk(points.begin(), points.begin() + 3);
	// 인덱스
	long long int idx = 3;
	// 순회
	while (true) {
		// 포인트
		Point point_1 = stk[stk.size() - 2];
		Point point_2 = stk[stk.size() - 1];
		// 기준 포인트 설정
		point_1.origin_point = { stk[stk.size() - 3].x, stk[stk.size() - 3].y };
		point_2.origin_point = { stk[stk.size() - 3].x, stk[stk.size() - 3].y };
		// 세 점이 반시계방향으로 정렬되어있으면
		if (!sort_clock_wise(point_1, point_2)) {
			// 중간점 삭제
			stk.erase(stk.end() - 2);
		}
		// 시계방향이거나 직선상에 있으면
		else {
			Point point_3 = stk[stk.size() - 3];
			// 직선상에 있으면
			if (ccw(point_3, point_1, point_2) == 0) {
				// 중간점 삭제
				stk.erase(stk.end() - 2);
			}
			// 시계방향이면
			else {
				// 모두 순회하면 끝
				if (idx >= points.size()) break;
				// 스택에 다음 점 추가
				stk.push_back(points[idx]);
				// 인덱스 최신화
				idx += 1;
			}
		}
		// 스택의 크기가 2 이하면
		if (stk.size() <= 2) {
			// 모두 순회하면 끝
			if (idx >= points.size()) break;
			// 스택에 다음 점 추가
			stk.push_back(points[idx]);
			// 인덱스 최신화
			idx += 1;
		}
	}

	return stk;
}

int main(void) {
	// 입력
	long long int N;
	cin >> N;
	// 점을 저장
	vector<Point> points;
	for (int i = 0; i < N; i++) {
		Point point;
		cin >> point.x >> point.y;
		points.push_back(point);
	}
	// 점을 x 기준, y 기준 으로 정렬
	sort(points.begin(), points.end(), sort_point);

	// 기준점 초기화
	for (int i = 0; i < N; i++) {
		points[i].origin_point = { points[0].x, points[0].y };
	}
	// 점을 시계방향으로 정렬
	sort(points.begin(), points.end(), sort_clock_wise);

	/*
	cout << "[ ";
	for (auto pt : points) {
		cout << "[ " << pt.x << ", " << pt.y << " ], ";
	}
	cout << "]\n";
	*/

	// 그라함 스캔
	vector<Point> convex_hull = graham_scan(points);

	/*
	cout << "[ ";
	for (auto pt : convex_hull) {
		cout << "[ " << pt.x << ", " << pt.y << " ], ";
	}
	cout << "]";
	*/

	cout << convex_hull.size();
}