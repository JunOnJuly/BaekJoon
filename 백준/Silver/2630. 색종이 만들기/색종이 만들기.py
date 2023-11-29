def solution(N, data_list):
    # 카운트
    global white
    global blue
    white = 0
    blue = 0
    # 재귀함수 호출
    split_paper(data_list, [0, N], [0, N])
    print(white)
    print(blue)


# 구간을 쪼개는 함수
def split_paper(data_list, x_range, y_range):
    # 카운트
    global white
    global blue
    # 타겟 좌표
    x_start, x_end = x_range
    y_start, y_end = y_range
    # 한칸이면 끝
    if x_end - x_start == 1:
        # 색 판별
        if data_list[x_start][y_start]:
            blue += 1
        else:
            white += 1
        return
    # 모두 같은 색인지 판별
    # 모두 같은 색이면
    state, color = check_all_color(data_list, x_range, y_range)
    if state:
        # 파란색이면
        if color == 1:
            blue += 1
        # 흰색이면
        else:
            white += 1
        return
    # 아니면
    else:
        # 순회하면서 재귀
        for split_x in [[x_start, (x_start+x_end)//2], [(x_start+x_end)//2, x_end]]:
            for split_y in [[y_start, (y_start+y_end)//2], [(y_start+y_end)//2, y_end]]:
                split_paper(data_list, split_x, split_y)


# 모두 같은 색인지 판별하는 함수
def check_all_color(data_list, x_range, y_range):
    # 타겟 좌표
    x_start, x_end = x_range
    y_start, y_end = y_range
    # 초기 세팅
    color = -1
    # 모두 같은 색인지 판별
    for x in range(x_start, x_end):
        for y in range(y_start, y_end):
            # 첫 칸의 색
            if color == -1:
                color = data_list[x][y]
            else:
                # 다른 색이 존재하면
                if color != data_list[x][y]:
                    return False, color
    # 모두 같은 색이면
    return True, color


N = int(input())
data_list = [list(map(int, input().split())) for _ in range(N)]
solution(N, data_list)