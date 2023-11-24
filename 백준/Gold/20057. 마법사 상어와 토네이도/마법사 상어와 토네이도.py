def solution(N, data_list):
    # 초반 모래의 양
    init_sum_sand = 0
    for data in data_list:
        init_sum_sand += sum(data)
    # 이동 거리
    move_length = 1
    # 이동 방향
    move_dir = -1
    # 현재 위치
    now_x = N//2
    now_y = N//2
    # 순회하며 탐색
    while True:
        for _ in range(2):
            # 이동 방향 + 1
            move_dir += 1
            for __ in range(move_length):
                # 토네이도 이동
                now_x, now_y = move_tornado(move_dir, now_x, now_y)
                # 모래 이동
                data_list = move_sand(data_list, now_x, now_y, move_dir, N)
                # 0, 0 에 도달하면 끝
                if not now_x and not now_y:
                    # 맵에 남아있는 모래의 양
                    left_sum_sand = 0
                    for data in data_list:
                        left_sum_sand += sum(data)
                    # 처음 모래의 양 - 남은 모래의 양
                    return init_sum_sand - left_sum_sand
        # 두 번 꺾이면 이동거리 + 1
        move_length += 1


# 토네이도가 이동하는 함수
def move_tornado(move_dir, now_x, now_y):
    # 이동 가이드
    move_guide_x = [0, 1, 0, -1]
    move_guide_y = [-1, 0, 1, 0]
    # 토네이도 위치
    return now_x + move_guide_x[move_dir%4], now_y + move_guide_y[move_dir%4]
    

# 모래가 이동하는 함수
def move_sand(data_list, now_x, now_y, move_dir, N):
    # 현 위치에 남은 모래
    left_sand = data_list[now_x][now_y]
    # 모래 이동 가이드
    sand_move_guide_x = [-2, -1, -1, -1, 0, 1, 1, 1, 2, 0]
    sand_move_guide_y = [0, -1, 0, 1, -2, -1, 0, 1, 0, -1]
    sand_move_value = [2, 10, 7, 1, 5, 10, 7, 1, 2, -1]
    # 현 위치의 모래량
    now_sand_value = data_list[now_x][now_y]
    # 가이드를 순회하며 모래 이동
    for sand_x, sand_y, sand_value in zip(sand_move_guide_x,\
                                          sand_move_guide_y,\
                                            sand_move_value):
        # 이동 방향 분기
        if move_dir%4 == 0:
            # 모래가 날아갈 위치
            sand_moved_x = now_x + sand_x
            sand_moved_y = now_y + sand_y
        elif move_dir%4 == 1:
            # 모래가 날아갈 위치
            sand_moved_x = now_x - sand_y
            sand_moved_y = now_y + sand_x
        elif move_dir%4 == 2:
            # 모래가 날아갈 위치
            sand_moved_x = now_x - sand_x
            sand_moved_y = now_y - sand_y
        else:
            # 모래가 날아갈 위치
            sand_moved_x = now_x + sand_y
            sand_moved_y = now_y - sand_x

        # 날아갈 위치가 유효하면
        if (sand_moved_x >=0 and sand_moved_x < N) and \
            (sand_moved_y >= 0 and sand_moved_y < N):
            # 마지막 alpha 에는 남은 모래 모두 이동
            if sand_value == -1:
                data_list[sand_moved_x][sand_moved_y] += left_sand
            else:
                # 날아갈 모래
                moving_sand = int(now_sand_value * (sand_value / 100))
                # 모래 날리기
                data_list[sand_moved_x][sand_moved_y] += moving_sand
                # 모래 빼주기
                left_sand -= moving_sand
        # 날아갈 위치가 유효하지 않으면
        else:
            # 날아갈 모래
            moving_sand = int(now_sand_value * (sand_value / 100))
            # 모래 빼주기
            left_sand -= moving_sand

    # 현 위치의 모래를 0으로 바꾸기
    data_list[now_x][now_y] = 0
    return data_list


N = int(input())
data_list = [list(map(int, input().split())) for _ in range(N)]
print(solution(N, data_list))