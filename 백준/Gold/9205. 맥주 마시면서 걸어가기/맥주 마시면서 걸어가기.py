from collections import deque


def solution(n, field):
    # 맵 정리
    start, field = field[0], field[1:]
    # BFS 로 풀거
    que = deque([start])
    # 방문 기록
    visited = [1 for _ in range(n+1)]

    while True:
        # 이동 가능 위치가 없으면
        if not que:
            return 'sad'
        # 현재 위치
        now = que.popleft()
        # 도착하면
        if not visited[-1]:
            return 'happy'
        for idx, store in enumerate(field):
            # 이동 가능 거리에 있고 방문한 적 없으면
            if (cal_distance(now, store) <= 1000) and \
                (visited[idx]):
                que.append(store)
                visited[idx] = 0


# 거리 계산
def cal_distance(idx1, idx2):
    return abs(idx1[0] - idx2[0]) + abs(idx1[1] - idx2[1])


t = int(input())

for _ in range(t):
    n = int(input())
    field = [list(map(int, input().split())) for _ in range(n+2)]
    print(solution(n, field))