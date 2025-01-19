import sys
from collections import deque

input = sys.stdin.readline


def solution(N, M, heights):
    # 봉우리 카운트
    cnt = 0
    # 방문 목록
    visited = [[0 for _ in range(M)] for __ in range(N)]
    # 탐색 위치
    move_dir = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [-1, -1], [1, -1], [-1, 1]]
    # 큐
    q = deque()
    # 순회
    while True:
        # 큐가 비어있으면
        if not q:
            # 방문하지 않은 위치 큐에 넣기
            for i in range(N):
                if not q:
                    for j in range(M):
                        if not visited[i][j]:
                            q.append([i, j])
                            # 방문 체크
                            visited[i][j] = 1
                            break
                
                else:
                    break
        
        # 그래도 큐가 비어있으면
        if not q:
            # 끝
            break
            
        # 현재 탐색하는 위치가 봉우리인지
        is_peak = 1
        # 순회
        while q:
            # 현재 위치
            now_x, now_y = q.popleft()
            # 현재 높이
            now_height = heights[now_x][now_y]
            # 다음 위치 탐색
            for x, y in move_dir:
                next_x = now_x + x
                next_y = now_y + y
                # 다음 위치가 인덱스 범위 내면
                if (next_x >= 0 and next_x < N and 
                    next_y >= 0 and next_y < M):
                    # 다음 위치의 높이
                    next_height = heights[next_x][next_y]
                    # 다음 위치의 높이가 현재 위치의 높이와 같으면
                    if next_height == now_height:
                        # 방문하지 않았다면
                        if not visited[next_x][next_y]:
                            # 방문
                            visited[next_x][next_y] = 1
                            # 큐에 삽입
                            q.append([next_x, next_y])

                    # 다음 위치의 높이가 현재 위치의 높이보다 높으면
                    elif next_height > now_height:
                        # 봉우리가 아님
                        is_peak = 0

        # 봉우리 카운트
        cnt += is_peak
    
    print(cnt)


# 입력
N, M = map(int, input().strip().split())
heights = [list(map(int, input().strip().split())) for _ in range(N)]

solution(N, M, heights)