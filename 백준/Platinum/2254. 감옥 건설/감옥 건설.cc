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
	// 기준 좌표
	long long int org_x;
	long long int org_y;
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

// 포인트 검색 함수
bool find_point(vector<Point>& pt_vec, Point& pt) {
	// 제거된 점이 존재하면
	if (!pt_vec.empty()) {
		for (int i = 0; i < pt_vec.size(); i++) {
			if (pt_vec[i].x == pt.x and pt_vec[i].y == pt.y) return true;
		}
		return false;
	}
	// 존재하지 않으면
	else {
		return false;
	}
}

// convex hull
vector<Point> convex_hull(vector<Point>& pillars, Point& pt_prison) {
	// 마지막으로 푸시된 기둥 인덱스
	int last_idx{};
	// 스택
	vector<Point> stk = { pillars[0] };
	// 기둥 순회
	while (true) {
		// 스택에 기둥이 두 개 미만이면 푸시
		if (stk.size() < 2) {
			// 마지막 기둥이면 끝
			if (last_idx >= pillars.size() - 1) break;
			for (int i = last_idx + 1; i < pillars.size(); i++) {
				// 스택에 푸시
				stk.push_back(pillars[i]);
				// 마지막으로 푸시한 기둥 인덱스
				last_idx = i;
				break;
			}
			continue;
		}
		//// 마지막 두 기둥이 감옥과 일직선상에 위치하는지 판별
		long long int CCW_prison = ccw(stk[stk.size() - 1], stk[stk.size() - 2], pt_prison);
		// 일직선상에 위치하면
		if (CCW_prison == 0) {
			// 팝
			stk.pop_back();
			continue;
		}
		// 스택에 기둥이 세 개 미만이면 푸시
		if (stk.size() < 3) {
			// 마지막 기둥이면 끝
			if (last_idx >= pillars.size() - 1) break;
			for (int i = last_idx + 1; i < pillars.size(); i++) {
				// 스택에 푸시
				stk.push_back(pillars[i]);
				// 마지막으로 푸시한 기둥 인덱스
				last_idx = i;
				break;
			}
			continue;
		}
		// 마지막 세 기둥의 방향 판별
		long long int CCW = ccw(stk[stk.size() - 3], stk[stk.size() - 2], stk[stk.size() - 1]);
		// 음수 ( 시계 방향 ) 거나 0 ( 일직선 ) 이면 다음 포인트 스택에 추가
		if (CCW <= 0) {
			// 마지막 기둥이면 끝
			if (last_idx >= pillars.size() - 1) break;
			for (int i = last_idx + 1; i < pillars.size(); i++) {
				// 스택에 푸시
				stk.push_back(pillars[i]);
				// 마지막으로 푸시한 기둥 인덱스
				last_idx = i;
				break;
			}
			continue;
		}
		// 양수 ( 반시계 방향 ) 이면 중간 포인트 삭제
		else {
			stk.erase(stk.end() - 2);
			continue;
		}
	}

	return stk;
}

// x, y 오름차순 정렬 함수
bool sort_pillar(Point& pt_1, Point& pt_2) {
	if (pt_1.x < pt_2.x) return true;
	else if (pt_1.x == pt_2.x and pt_1.y < pt_2.y) return true;
	else return false;
}

// 두 점 거리 계산
float cal_dist(Point& pt_1, Point& pt_2) {
	// 각 좌표 차
	long long int sub_x = pt_1.x - pt_2.x;
	long long int sub_y = pt_1.y - pt_2.y;
	// 계산
	return sqrt(pow(sub_x, 2) + pow(sub_y, 2));
}

// 시계방향 정렬 함수
bool sort_clockwise(Point& pt_1, Point& pt_2) {
	// 기준점
	Point origin_pt = Point({ pt_1.org_x, pt_1.org_y });
	// ccw 값
	long long int CCW = ccw(origin_pt, pt_1, pt_2);
	// ccw 값이 음수면 시계 방향
	if (CCW < 0) return true;
	// ccw 값이 양수면 반시계 방향
	else if (CCW > 0) return false;
	// 0 이면 직선, 가까운 점이 앞으로
	else {
		if (cal_dist(origin_pt, pt_1) < cal_dist(origin_pt, pt_2)) return true;
		else return false;
	}
}

// 교도소가 껍질에 포함되는지 판별하는 함수
bool is_include_prison(vector<Point>& hull, Point& pt_prison) {
	// 한정된 정수 좌표평면의 어느점도 포함하지 않는 임의의 반직선
	Line line_org = { pt_prison, Point({200001, pt_prison.y + 1}) };
	// 껍질의 끝 인덱스와 시작 인덱스에 선분 추가
	hull.push_back(hull[0]);
	// 껍질과 반직선이 교차하는지 카운트
	int cross_count = 0;
	// 껍질을 구성하는 선분 순회
	for (int i = 0; i < hull.size() - 1;i++) {
		// 껍질을 구성하는 선분
		Line hull_line({ hull[i], hull[i + 1] });
		// 교차하면 카운트 + 1
		if (is_cross(line_org, hull_line)) cross_count += 1;
	}
	// 카운트가 홀수면 포함됨
	if (cross_count % 2 == 1) return true;
	else return false;
}

int main(void) {
	//// 최외각 convex hull -> 점 제거 -> 반복
	// 리스트 x, y좌표 기준으로 정렬
	// 리스트 시계방향으로 정렬
	// ccw 알고리즘 최외곽 판정
	// 판정되면 제거
	
	//// 담 중 중앙점과 일직선 제외
	// ccw 알고리즘 일직선 판별\
	
	// 입력
	int N, px, py;
	cin >> N >> px >> py;
	// 감옥 위치
	Point pt_prison = { px, py };
	// 기둥 위치 저장할 벡터
	vector<Point> pillars;
	for (int i = 0; i < N; i++) {
		Point pt;
		cin >> pt.x >> pt.y;
		pillars.push_back(pt);
	}
	// 기둥 위치 x, y 오름차순 정렬
	sort(pillars.begin(), pillars.end(), sort_pillar);
	// 껍질들
	vector<vector<Point>> hulls;
	// convex hull
	while (!pillars.empty()) {
		// 기준 좌표 설정
		for (int i = 1; i < pillars.size(); i++) {
			pillars[i].org_x = pillars[0].x;
			pillars[i].org_y = pillars[0].y;
		}
		// 기둥 위치 시계방향 정렬
		sort(pillars.begin(), pillars.end(), sort_clockwise);
		// 나온 껍질은 제거대상 포인트
		vector<Point> remove_points = convex_hull(pillars, pt_prison);
		// 껍질 보관
		hulls.push_back(remove_points);
		// 껍질에 포함된 점들 제외
		for (auto pt : remove_points) {
			for (auto iter = pillars.begin(); iter != pillars.end(); iter++) {
				if (pt.x == (*iter).x and pt.y == (*iter).y) {
					pillars.erase(iter);
					break;
				}
			}
		}
	}
	// 교도소가 껍질에 포함되는 횟수
	int include_count = 0;
	// 교도소가 각 껍질에 포함되는지 판별
	for (auto hull : hulls) {
		// 포함되면 카운트
		if (is_include_prison(hull, pt_prison)) include_count += 1;
	}
	cout << include_count;
}