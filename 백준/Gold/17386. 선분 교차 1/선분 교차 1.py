def solution(x1, y1, x2, y2, x3, y3, x4, y4):
    # CCW 알고리즘은 기본적으로 주어진 점선들의 회전방향을 알 수 있음
    # 어떤 직선을 기준으로 두 점이 양방향에 있으면 직선과 각 점을 이었을 때 회전방향은 반대임
    # 각 선분을 기준으로 나머지 선분의 각 점이 이루는 회전방향이 모두 다르면
    # 각 선분을 이루는 점은 나머지 선분을 기준으로 반대쪽에 있음 -> 교차함
    # 선분 리스트
    line_list = [[x1, y1, x2, y2], [x3, y3, x4, y4]]
    for i in range(2):
        # 선분
        line = line_list[i]
        mul_ccw = 1
        for j in range(2):
            # 점
            point = line_list[1-i][2*j:2*j+2]
            ccw = CCW(line, point)
            # ccw 가 0 이면 점이 선 위에 있으면 겹침, 아니면 안겹침
            if ccw == 0:
                # x, y 의 범위로 결정
                if ((point[0] >= line[0] and point[0] <= line[3]) or (point[0] >= line[0] and point[0] <= line[3])) and \
                    ((y1 >= y3 and y1 <= y4) or (y1 <= y3 and y1 >= y4)):
                    print(1)
                    return
                else:
                    print(0)
                    return
            mul_ccw *= ccw
        if mul_ccw > 0:
            print(0)
            return
        else:
            if i == 1:
                print(1)
                return
            

# CCW
def CCW(line, point):
    # x, y 리스트
    x_list = []
    y_list = []
    for i in range(0, 4, 2):
        x_list.append(line[i])
        y_list.append(line[i+1])
    x_list.append(point[0])
    y_list.append(point[1])
    x_list.append(line[0])
    y_list.append(line[1])
    # 합
    ccw_sum = 0
    for idx in range(3):
        ccw_sum += x_list[idx]*y_list[idx+1]
        ccw_sum -= y_list[idx]*x_list[idx+1]
    return ccw_sum


x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())
solution(x1, y1, x2, y2, x3, y3, x4, y4)