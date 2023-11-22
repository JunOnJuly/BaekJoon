from collections import deque

def solution(N, K, L, apple_list, dir_list):
    # 맵
    # 0 빈공간 1 사과 2 뱀
    data_map = [[0 for _ in range(N)] for __ in range(N)]
    for apple in apple_list:
        data_map[apple[0]-1][apple[1]-1] = 1
    data_map[0][0] = 2
    # 이동 가이드, 오른쪽 시작/시계방향
    move_guide_x = [0, 1, 0, -1]
    move_guide_y = [1, 0, -1, 0]
    # 뱀
    snake = deque([[0, 0]])
    # 뱀의 방향, 뺄 경우를 대비해서 100으로 세팅
    snake_dir = 100
    # 방향 리스트 인덱스
    idx_dir_list = 0
    # 지난 시간
    sec = 0
    # 규칙 순회
    while True:
        # 시간 최신화
        sec += 1
        # 뱀 이동
        # 다음 좌표
        next_x = snake[-1][0]+move_guide_x[snake_dir%4]
        next_y = snake[-1][1]+move_guide_y[snake_dir%4]
        # 이동가능하면 이동, 인덱스 내부일 때/뱀이 아니면
        if (next_x >= 0 and next_x < N) and \
            (next_y >= 0 and next_y < N) and \
            (data_map[next_x][next_y] != 2):
            # 사과가 아니면 꼬리 삭제
            if data_map[next_x][next_y] != 1:
                # 이동
                snake.append([next_x, next_y])
                data_map[next_x][next_y] = 2
                # 마지막 꼬리
                last_tale = snake.popleft()
                data_map[last_tale[0]][last_tale[1]] = 0
            # 사과면 추가만 함
            else:
                # 이동
                snake.append([next_x, next_y])
                data_map[next_x][next_y] = 2
        # 이동 불가능하면 끝
        else:
            return sec
        
        # 다음 회전 시간, 방향
        next_time, next_dir = dir_list[idx_dir_list]
        # 회전 시간이 되면
        if sec == int(next_time):
            # 왼쪽
            if next_dir == 'L':
                snake_dir -= 1
            else:
                snake_dir += 1

            # 회전 규칙 업데이트
            # 회전 규칙의 마지막이 아니면
            if idx_dir_list < len(dir_list)-1:
                idx_dir_list += 1


N = int(input())
K = int(input())
apple_list = [list(map(int, input().split())) for _ in range(K)]
L = int(input())
dir_list = [list(input().split()) for _ in range(L)]
print(solution(N, K, L, apple_list, dir_list))