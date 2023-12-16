def solution(N, data_list):
    # 데이터 x 좌표 y 좌표 분리
    x_list = []
    y_list = []
    for x, y in data_list:
        x_list.append(x)
        y_list.append(y)
    x_list.append(x_list[0])
    y_list.append(y_list[0])
    # 외적 합
    sum_cross = 0
    # 외적
    for i in range(N):
        sum_cross += x_list[i]*y_list[i+1]
        sum_cross -= y_list[i]*x_list[i+1]
    sum_cross = abs(sum_cross)/2
    print(f'{round(sum_cross, 1):.1f}')


N = int(input())
data_list = [list(map(int, input().split())) for _ in range(N)]
solution(N, data_list)