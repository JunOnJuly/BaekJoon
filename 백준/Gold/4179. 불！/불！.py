import sys
from collections import deque

input = sys.stdin.readline


def solution(R, C, labyr):
    # 불 데크
    fire_dq = deque()
    # 사람 데크
    hum_dq = deque()
    # 사람 방문 목록
    hum_visited = [[True for _ in range(C)] for __ in range(R)]
    # 미로 탐색하며 위치 체크
    for i in range(R):
        for j in range(C):
            # 불
            if labyr[i][j] == 'F':
                fire_dq.append([i, j, 0])

            # 사람
            elif labyr[i][j] == 'J':
                hum_dq.append([i, j, 0])
    
    # 이동 방향
    move_guide = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    # 순회
    # 불 카운트
    cnt = 0
    while hum_dq:
        ## 불 먼저 이동
        while fire_dq:
            # 이번 카운트까지
            if fire_dq[0][-1] != cnt:
                break

            # 불 위치 / 카운트
            f_now_x, f_now_y, f_cnt = fire_dq.popleft()
            # 위치 순회
            for x, y in move_guide:
                # 확산될 위치
                f_next_x = f_now_x + x
                f_next_y = f_now_y + y
                # 인덱스 범위 안이고 벽이 아니면
                if (f_next_x >= 0 and f_next_x < R) and (f_next_y >= 0 and f_next_y < C) and \
                    (labyr[f_next_x][f_next_y] not in ['#', 'F']):
                    # 불이 번짐
                    labyr[f_next_x][f_next_y] = 'F'
                    # 큐에 삽입
                    fire_dq.append([f_next_x, f_next_y, f_cnt+1])
        
        ## 사람 이동
        while hum_dq:
            # 이번 카운트까지
            if hum_dq[0][-1] != cnt:
                break

            # 사람 위치 / 카운트
            h_now_x, h_now_y, h_cnt = hum_dq.popleft()
            # 현재 위치가 가장자리면
            if h_now_x in [0, R-1] or h_now_y in [0, C-1]:
                print(h_cnt + 1)
                return
            
            # 위치 순회
            for x, y in move_guide:
                # 확산될 위치
                h_next_x = h_now_x + x
                h_next_y = h_now_y + y
                # 인덱스 범위 안이고 방문하지 않았고벽과 불이 아니면
                if (h_next_x >= 0 and h_next_x < R) and (h_next_y >= 0 and h_next_y < C) and \
                    (hum_visited[h_next_x][h_next_y]) and \
                    (labyr[h_next_x][h_next_y] not in ['#', 'F']):
                    # 이동
                    hum_dq.append([h_next_x, h_next_y, h_cnt+1])
                    # 방문 체크
                    hum_visited[h_next_x][h_next_y] = False
        
        # 카운트 + 1
        cnt += 1

    print('IMPOSSIBLE ')


# 입력
R, C = map(int, input().strip().split())
labyr = [list(input().strip()) for _ in range(R)]

solution(R, C, labyr)