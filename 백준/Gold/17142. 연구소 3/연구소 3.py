import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline


def solution(N, M, lab):
    # 바이러스 위치 탐색
    virs_idxs = [[i, j] for i in range(N) for j in range(N) if lab[i][j] == 2]
    # 이동 방향
    move_guide = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    # 최대 카운트의 최솟값
    min_max_cnt = float('inf')
    # M 개의 바이러스 위치 조합 순회
    for virs in combinations(virs_idxs, M):
        ## BFS
        # 데크
        dq = deque(map(lambda x: x+[0], virs))
        # 방문 목록
        visited = [[-1 for _ in range(N)] for __ in range(N)]
        for i, j in virs:
            visited[i][j] = 0

        # 순회
        while dq:
            # 현재 인덱스, 카운트
            now_x, now_y, now_cnt = dq.popleft()
            # 이동 가능 방향 순회
            for x, y in move_guide:
                # 다음 인덱스
                next_x = now_x + x
                next_y = now_y + y
                # 이동 가능하면
                if (next_x >= 0 and next_x < N) and (next_y >= 0 and next_y < N) and \
                    (lab[next_x][next_y] != 1) and \
                    (visited[next_x][next_y] < 0):
                    # 방문 체크
                    visited[next_x][next_y] = now_cnt + 1
                    # 데크에 추가
                    dq.append([next_x, next_y, now_cnt + 1])

        # 벽이 아닌 위치에 도달하는 카운트
        cnts = [visited[i][j] for i in range(N) for j in range(N) if lab[i][j] == 0]
        # 모든 위치에 방문했으면
        if cnts and all([cnt >= 0 for cnt in cnts]):
            # 최대 카운터의 최솟값 갱신
            min_max_cnt = min(min_max_cnt, max(cnts))
        
        # 모든 위치가 벽 혹은 바이러스면
        elif not cnts:
            min_max_cnt = 0

    print(min_max_cnt if min_max_cnt != float('inf') else -1)


# 입력
N, M = map(int, input().strip().split())
lab = [list(map(int, input().strip().split())) for _ in range(N)]

solution(N, M, lab)