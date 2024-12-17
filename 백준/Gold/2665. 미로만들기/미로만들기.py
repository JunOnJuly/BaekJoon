import sys
import heapq as hq

input = sys.stdin.readline


def solution(n, rooms):
    # 이동 방향
    move_dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    # 방문 목록
    visited = [[float('inf') for _ in range(n)] for __ in range(n)]
    # 큐 / [[바꾼 수, 인덱스] ... ]
    q = [[0, 0, 0]]
    visited[0][0] = 0
    # 순회
    while q:
        # 바꾼 수 / 인덱스
        changed, now_x, now_y = hq.heappop(q)
        # 바꾼 수가 더 많으면 패스
        if changed > visited[now_x][now_y]:
            continue
        
        # 이동 가능 위치 순회
        for x, y in move_dirs:
            # 다음 인덱스
            next_x = now_x + x
            next_y = now_y + y
            # 범위 내고
            if (next_x >= 0 and next_x < n) and (next_y >= 0 and next_y < n):
                # 벽이 아니면서 더 적게 바꾸고 방문할 수 있으면
                if (rooms[next_x][next_y] == '1') and (changed < visited[next_x][next_y]):
                    # 방문
                    visited[next_x][next_y] = changed
                    # 큐에 추가
                    hq.heappush(q, [changed, next_x, next_y])
                
                # 벽인데 더 적게 바꾸고 방문할 수 있으면
                elif (rooms[next_x][next_y] == '0') and (changed + 1 < visited[next_x][next_y]):
                    # 방문
                    visited[next_x][next_y] = changed + 1
                    # 큐에 추가
                    hq.heappush(q, [changed+1, next_x, next_y])
        
    print(visited[-1][-1])


# 입력
n = int(input().strip())
rooms = [input().strip() for _ in range(n)]

solution(n, rooms)