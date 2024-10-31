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


    # 볼록 껍질 중 가장 먼 거리 계산
    max_dist = 0
    for i in range(len(convex_hull)-1):
        for j in range(i, len(convex_hull)):
            max_dist = max(max_dist, cal_dist(convex_hull[i], convex_hull[j]))
    
    print(pow(max_dist, 1/2))


# 입력
C = int(input().strip())
arrows = [list(map(int, input().strip().split())) for _ in range(C)]

solution(C, arrows)