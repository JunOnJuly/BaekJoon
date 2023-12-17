import math


def solution(data_list):
    # x, y 좌표 분리
    x_list = []
    y_list = []
    for x, y in data_list:
        x_list.append(x)
        y_list.append(y)
    x_list.append(data_list[0][0])
    y_list.append(data_list[0][1])
    # CCW 알고리즘
    sum_ccw = 0
    for i in range(3):
        sum_ccw += x_list[i]*y_list[i+1]
        sum_ccw -= y_list[i]*x_list[i+1]
    # 합이 0 이상이면 반시계
    # 합이 0 이하면 시계 
    # 합이 0 이면 일직선
    if sum_ccw > 0:
        print(1)
    elif sum_ccw < 0:
        print(-1)
    else:
        print(0)


data_list = [list(map(int, input().split())) for _ in range(3)]
solution(data_list)