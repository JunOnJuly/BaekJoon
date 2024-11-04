import sys
from functools import cmp_to_key
from dataclasses import dataclass
import math

input = sys.stdin.readline


# 점
@dataclass
class Point:
    x : int
    y : int
    origin_x : int = None
    origin_y : int = None


# 선
@dataclass
class Line:
    p1 : Point
    p2 : Point


# ccw
def ccw(line:Line, point:Point) -> int:
    # ccw 행렬
    ccw_mat = [[line.p1.x, line.p1.y],
               [line.p2.x, line.p2.y],
               [point.x, point.y],
               [line.p1.x, line.p1.y]]
    
    # 계산값
    result = 0
    # 계산
    for i in range(3):
        result += ccw_mat[i][0]*ccw_mat[i+1][1]
        result -= ccw_mat[i+1][0]*ccw_mat[i][1]
    
    # 리턴
    return result


# 거리 계산
def cal_distance_pp(p1:Point, p2:Point):
    delta_x = p1.x-p2.x
    delta_y = p1.y-p2.y
    
    return pow(pow(delta_x, 2) + pow(delta_y, 2), 1/2)


# 거리 계산 (선 / 점)
def cal_distance_lp(line:Line, point:Point):
    # 삼각형의 넓이
    tri_s = abs(ccw(line, point)) / 2
    # 변의 길이로 나누기
    dist = (tri_s / cal_distance_pp(line.p1, line.p2)) * 2

    return dist


# 시계방향으로 정렬
def sort_clockwise(p1:Point, p2:Point) -> int:
    # 기준점
    origin_point = Point(p1.origin_x, p1.origin_y)
    # ccw
    ccw_value = ccw(Line(origin_point, p1), p2)
    # 직선이면
    if not ccw_value:
        # 가까운 쪽이 앞으로
        return cal_distance_pp(origin_point, p1) > cal_distance_pp(origin_point, p2)

    # 직선이 아니면
    else:
        # 시계방향이면 그대로
        return ccw_value


def solution(T, n, idxs):
    # 우선 x / y 둘 중 하나로 정렬
    # 나는 x 로 정렬
    idxs = sorted(idxs, key=lambda x:x[0])
    # 인덱스들 포인트로 치환
    idxs = [Point(*idx, *idxs[0]) for idx in idxs]
    # 시계방향으로 정렬
    idxs = sorted(idxs, key=cmp_to_key(sort_clockwise))
    # 볼록 껍질
    convex_hull = idxs[:3]
    # 다음 인덱스
    next_idx = 3
    # 순회
    while True:
        # 볼록 껍질에 인덱스가 3 개 미만이면
        if len(convex_hull) < 3:
            # 모든 인덱스를 순회했으면 끝
            if next_idx >= n:
                break
            
            # 다음 인덱스 넣어주기
            convex_hull.append(idxs[next_idx])
            # 인덱스 업데이트
            next_idx += 1
        
        # 시계방향 판정
        ccw_value = ccw(Line(convex_hull[-3], convex_hull[-2]), convex_hull[-1])
        # 시계방향이면
        if ccw_value < 0:
            # 모든 인덱를 순회했으면 끝
            if next_idx >= n:
                break
            # 다음 점 추가
            convex_hull.append(idxs[next_idx])
            # 인덱스 업데이트
            next_idx += 1
        
        # 시계방향이 아니면
        else:
            # 중간 점 지우기
            convex_hull.pop(-2)
    
    convex_hull.append(convex_hull[0])
    # 도형의 폭 중 최솟값
    min_height = float('inf')
    # 볼록껍질의 변 순회
    for i in range(len(convex_hull)-1):
        # 변
        line = Line(convex_hull[i], convex_hull[i+1])
        # 해당 변에서 다른 점까지 거리의 최댓값
        max_height = 0
        # 변에서 볼록껍질에 속하는 점들 사이의 거리 측정
        for point in convex_hull:
            max_height = max(max_height, cal_distance_lp(line, point))

        # 도형의 폭 최솟값 갱신
        min_height = min(min_height, max_height)
    
    print(f'Case {T}: {math.ceil(min_height*100)/100:.2f}')


# 입력
T = 1
while True:
    n = int(input().strip())
    if not n:
        break

    idxs = [list(map(int, input().strip().split())) for _ in range(n)]

    solution(T, n, idxs)
    T += 1