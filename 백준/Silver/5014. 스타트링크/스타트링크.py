# BFS 쓸거라 deque
from collections import deque


def solution(F, S, G, U, D):
    # 선택지
    selects = [U, -D]
    # 방문한 위치
    visited = [1 if floor != S else 0 for floor in range(F+1)]
    que = deque([S])
    
    # 버튼 누른 횟수
    cnt = 0
    while True:
        # 목적 층에 방문했다면 끝
        if not visited[G]:
            return cnt
        # 도달할 수 없으면 끝
        if not que:
            return 'use the stairs'
        
        for _ in range(len(que)):
            # 현재 층
            now_floor = que.popleft()
            for select in selects:
                # 다음 예정 층
                next_floor = now_floor + select
                # 다음 예정 층이 건물 범위 안에 있고 방문 안했을 때
                if (next_floor < len(visited) and next_floor > 0) and visited[next_floor]:
                    que.append(next_floor)
                    visited[next_floor] = 0
        # 버튼 누른 횟수 추가
        cnt += 1
                    
                    
F, S, G, U, D = map(int, input().split())
print(solution(F, S, G, U, D))