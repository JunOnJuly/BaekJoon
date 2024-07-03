from math import sqrt


def cal_dist(x, y):
    return sqrt(pow(x, 2) + pow(y, 2))


def solution(k, d):
    # 점 카운트
    cnt = 0
    # 가장 먼 x 축 위의 점
    start_x = (d//k) * k
    start_y = 0
    # 순회
    while start_x >= 0:
        # 카운트 추가
        cnt += start_x//k + 1
        # y 이동
        start_y += k
        # 한계 거리를 넘지 않는 끝 점 찾기
        while start_x >= 0 and cal_dist(start_x, start_y) > d:
            start_x -= k
    
    return cnt