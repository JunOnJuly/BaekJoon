import sys
from collections import deque

input = sys.stdin.readline


def solution(N, M, cz_map):
    # 이동 방향
    move_dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    # 카운트
    cnt = 0
    # 치즈가 남지 않을 때 까지 순회
    while any([any(cz) for cz in cz_map]):
        # 방문 목록
        visited = [[0 for _ in range(M)] for __ in range(N)]
        # 시작 지점은 가장자리 중 하나
        q = deque([[0, 0]])
        # 순회
        while q:
            # 현재 위치
            now_x, now_y = q.popleft()
            # 이동방향 순회
            for x, y in move_dir:
                # 다음 위치
                next_x = now_x + x
                next_y = now_y + y
                # 다음 위치가 인덱스 범위 내에 있으면
                if (next_x >= 0 and next_x < N) and (next_y >= 0 and next_y < M):
                    # 다음 위치가 치즈가 아니고 방문하지 않았다면
                    if not cz_map[next_x][next_y] and not visited[next_x][next_y]:
                        # 방문 기록 
                        visited[next_x][next_y] = 1
                        # 큐에 넣기
                        q.append([next_x, next_y])
                    
                    # 다음 위치가 치즈면
                    elif cz_map[next_x][next_y]:
                        # 방문 기록
                        visited[next_x][next_y] += 1
        
        # 녹을 치즈 탐색
        for i in range(N):
            for j in range(M):
                # 방문횟수가 2 이상인 위치 탐색
                if visited[i][j] >= 2:
                    # 녹이기
                    cz_map[i][j] = 0
        
        # 카운트 더해주기
        cnt += 1
    
    print(cnt)
    

# 입력
N, M = map(int, input().strip().split())
cz_map = [list(map(int, input().strip().split())) for _ in range(N)]

solution(N, M, cz_map)