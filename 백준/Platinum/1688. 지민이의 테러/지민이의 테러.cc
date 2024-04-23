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
	long long int x;
	long long int y;
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

// 직선 데이터를 저장할 구조체
struct Line {
	// 속한 점들
	Point point_1;
	Point point_2;
};

// 교차하는지 판단
bool is_cross(Line line_1, Line line_2) {
	// ccw
	long long int ccw_1 = ccw(line_1.point_1, line_1.point_2, line_2.point_1);
	long long int ccw_2 = ccw(line_1.point_1, line_1.point_2, line_2.point_2);
	long long int ccw_3 = ccw(line_2.point_1, line_2.point_2, line_1.point_1);
	long long int ccw_4 = ccw(line_2.point_1, line_2.point_2, line_1.point_2);
	// 곱한 값들 노말라이즈
	long long int norm_ccw_1 = ccw_1 > 0 ? 1 : ccw == 0 ? 0 : -1;
	long long int norm_ccw_2 = ccw_2 > 0 ? 1 : ccw == 0 ? 0 : -1;
	long long int norm_ccw_3 = ccw_3 > 0 ? 1 : ccw == 0 ? 0 : -1;
	long long int norm_ccw_4 = ccw_4 > 0 ? 1 : ccw == 0 ? 0 : -1;
	// 결과
	long long int result_1 = norm_ccw_1 * norm_ccw_2;
	long long int result_2 = norm_ccw_3 * norm_ccw_4;
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

int main(void) {
	// 입력
	int N;
	cin >> N;
	// 방어막 점들을 저장할 벡터
	vector<Point> points;
	for (int i = 0; i < N; i++) {
		Point point;
		cin >> point.x >> point.y;
		points.push_back(point);
	}
	// 시작 점 마지막에 추가
	points.push_back(points.front());
	// 사람 위치를 저장할 어레이
	array<Point, 3> people;
	for (int i = 0; i < 3; i++) {
		Point point;
		cin >> point.x >> point.y;
		people[i] = point;
	}
	// 사람 목록 순회
	for (int i = 0; i < 3; i++) {
		// 현재 사람
		Point person = people[i];
		// x 축으로 무한히 뻗은 반직선과 방어막이 교차하는 횟수
		long long int cnt_cross = 0;
		// 현재 사람에서 x 축으로 무한히 뻗은 반직선
		// 다각형의 어떤 변도 포함하지 않는 직선을 만들기 위해 기울기 조정
		// person.x -> 1000000000 (시스템상 최대 x) * 2 + 1 / person.y -> person.y + 1 을 지나는 직선에 포함되는 직선은 해당 범위의 정수 좌표계에선 만들 수 없음
		long long int max_x = 2000000001;
		long long int max_y = person.y + 1;
		Line person_line = { person, Point({max_x, max_y}) };
		// 방어막 점들이 지나는 직선 순회
		for (int i = 0; i < N; i++) {
			// 사람의 인덱스가 직선 위에 있으면 출력하고 패스
			if (person.x >= min(points[i].x, points[i + 1].x) and person.x <= max(points[i].x, points[i + 1].x) and
				person.y >= min(points[i].y, points[i + 1].y) and person.y <= max(points[i].y, points[i + 1].y) and
				ccw(points[i], points[i + 1], person) == 0) {
				cout << 1 << "\n";
				break;
			}
			// 직선 중 어느 점도 사람의 인덱스과 같지 않으면
			else {
				// 방어막 직선
				Line barrier_line = { points[i], points[i + 1] };
				// 교차하면 cnt + 1
				if (is_cross(person_line, barrier_line)) {
					cnt_cross += 1;
				}
			}
			// 마지막 직선을 순회한 후
			if (i == N - 1) {
				// 교차하는 점의 수가 홀수이면 내부 / 짝수이면 외부
				if (cnt_cross % 2 == 0) {
					cout << 0 << "\n";
				}
				else {
					cout << 1 << "\n";
				}
			}
		}
	}
}