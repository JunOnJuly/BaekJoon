import sys
import heapq

input = sys.stdin.readline


def solution(M, N, data_map):
    # 이동 가이드
    move_guide = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    # 방문 횟수 리스트
    visited = [[0 for _ in range(N)] for __ in range(M)]
    visited[0][0] = 1
    # 큐
    hq = [[-data_map[0][0], [0, 0]]]
    # 순회
    while hq:
        # 현재 높이, 현재 인덱스
        now_height, [now_x, now_y] = heapq.heappop(hq)
        now_height *= -1
        # 이동 가능한 위치 순회
        for x, y in move_guide:
            # 다음 인덱스
            next_x, next_y = now_x + x, now_y + y
            # 이동 가능한 위치면
            if (next_x >= 0 and next_x < M) and (next_y >= 0 and next_y < N):
                # 다음 위치의 높이가 더 낮으면
                if data_map[next_x][next_y] < now_height:
                    # 방문한 적이 없다면
                    if not visited[next_x][next_y]:
                        # 큐에 삽입
                        heapq.heappush(hq, [-data_map[next_x][next_y], [next_x, next_y]])
                    # 방문 횟수 최신화
                    visited[next_x][next_y] += visited[now_x][now_y]


    return visited[M-1][N-1]



# 입력
M, N = map(int, input().strip().split())
data_map = [list(map(int, input().strip().split())) for _ in range(M)]

print(solution(M, N, data_map))