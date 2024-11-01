import sys
from dataclasses import dataclass
from functools import cmp_to_key

input = sys.stdin.readline


# Point
@dataclass
class Point:
    x: int
    y: int
    # 정렬을 위한 기준점
    origin_x: int = 0
    origin_y: int = 0


# Line
@dataclass
class Line:
    point1: Point
    point2: Point


# CCW
def ccw(line: Line, point: Point):
    # ccw 계산
    result = ((line.point2.x - line.point1.x)*(point.y - line.point1.y)
              -(point.x - line.point1.x)*(line.point2.y - line.point1.y))
    
    # 결과 압축
    if result > 0:
        return 1

    elif result < 0:
        return -1

    else:
        return 0


# 거리 계산
def cal_dist(point: Point, sub_point: Point = None):
    if sub_point:
        return pow(point.x - sub_point.x, 2) + pow(point.y - sub_point.y, 2)

    return pow(point.x - point.origin_x, 2) + pow(point.y - point.origin_y, 2)


# 시계 방향으로 정렬
def sort_to_clockwise(point1: Point, point2: Point):
    # ccw
    line = Line(Point(point1.origin_x, point1.origin_y), point1)
    result = ccw(line, point2)
    ## 시계방향으로 정렬
    # 일직선이면 가까운 점 우선
    if result == 0:
        return cal_dist(point1) - cal_dist(point2)
    
    else:
        return result
    

def solution(C, arrows):
    # 가장 먼 화살쌍은 볼록껍질에 포함되어 있을 것
    # 좌표들을 우선 x 기준으로 정렬
    arrows = sorted(arrows, key=lambda x: (x[0], x[1]))
    # arrows Point로 치환
    arrows = [Point(*arrows[i], *arrows[0]) for i in range(len(arrows))]
    # 시계 방향으로 정렬
    arrows = sorted(arrows, key=cmp_to_key(sort_to_clockwise))
    # 그라함 스캔
    arrows = arrows
    # 볼록 껍질
    convex_hull = arrows[:3]
    # 점 인덱스
    point_idx = 3
    # 순회
    while True:
        # 볼록 껍질 내부에 점이 두 개 이하면 점 추가
        if len(convex_hull) <= 2:
            # 점 인덱스가 점들의 수를 넘으면 끝
            if point_idx >= len(arrows):
                break

            convex_hull.append(arrows[point_idx])
            point_idx += 1
            continue
        
        ## 볼록 껍질 내부의 시계방향 판단
        # ccw
        result = ccw(Line(convex_hull[-3], convex_hull[-2]), convex_hull[-1])
        # 시계 방향이면
        if result < 0:
            # 점 인덱스가 점들의 수를 넘으면 끝
            if point_idx >= len(arrows):
                break 
            
            # 점 추가
            convex_hull.append(arrows[point_idx])
            point_idx += 1
            continue

        # 아니면
        else:
            # 가운데 점 제거
            convex_hull.pop(-2)

    ## 회전하는 캘리퍼스
    # 두 벡터의 기준점
    origin_idx = 0
    comp_idx = 1
    # 기준 벡터가 움직였는지 여부
    is_origin_move = False
    # 볼록껍질의 포인트 수
    convex_num = len(convex_hull)
    # 거리의 최댓값
    max_dist = 0
    # 최대 거리일 때 인덱스
    max_idxs = [0, 1]
    # 회전
    # 기준 벡터가 이동했고 원점으로 돌아왔으면 끝
    while not is_origin_move or origin_idx:
        # 두 벡터
        origin_vec = Line(convex_hull[origin_idx%convex_num], convex_hull[(origin_idx+1)%convex_num])
        comp_vec = Line(convex_hull[comp_idx%convex_num], convex_hull[(comp_idx+1)%convex_num])
        # 최장거리
        dist = cal_dist(origin_vec.point1, comp_vec.point1)
        # 거리가 최장거리면
        if dist > max_dist:
            # 최장거리 최신화
            max_dist = dist
            # 최대거리 인덱스
            max_idxs = [origin_vec.point1, comp_vec.point1]

        # 두 벡터의 사이각
        ccw_vec = ccw(origin_vec, Point(comp_vec.point2.x-(comp_vec.point1.x-origin_vec.point2.x), comp_vec.point2.y-(comp_vec.point1.y-origin_vec.point2.y)))
        # 두 벡터의 사이각이 반시계방향이면
        if ccw_vec >= 0:
            # 기준 벡터 이동
            origin_idx = (origin_idx+1)%convex_num
            # 기준 벡터 이동 체크
            is_origin_move = True
        
        # 두 벡터의 사이각이 시계방향이면
        else:
            # 비교 벡터 이동
            comp_idx = (comp_idx+1)%convex_num

    print(f'{max_idxs[0].x} {max_idxs[0].y} {max_idxs[1].x} {max_idxs[1].y}')


# 입력
T = int(input().strip())
for _ in range(T):
    C = int(input().strip())
    arrows = [list(map(int, input().strip().split())) for _ in range(C)]

    solution(C, arrows)