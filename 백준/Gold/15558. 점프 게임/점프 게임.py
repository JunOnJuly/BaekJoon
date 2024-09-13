import sys
from collections import deque
from copy import deepcopy

input = sys.stdin.readline


def solution(N, K, data_list):
    # 큐 / 인덱스, 이동 횟수
    dq = deque([[[0, 0], 0]])
    # 방문 목록
    visited = deepcopy(data_list)
    # 순회
    while dq:
        # 현재 위치
        [now_x, now_y], cnt = dq.popleft()
        # 카운트보다 작은 위치 이동 불가 체크
        if cnt:
            for i in range(2):
                visited[i][cnt-1] = 0    
        # 현재 위치가 사라졌다면 다음
        if not visited[now_x][now_y]:
            continue
        # 방문 체크
        visited[now_x][now_y] = 0
        # 이동 후보 순회
        for next_x, next_y in [[1-now_x, now_y+K], [now_x, now_y+1], [now_x, now_y-1]]:
            # N 을 넘어갔으면
            if next_y >= N:
                return 1
            # 아직 안넘었고 방문한 적 없고 인덱스 범위 안이라면
            elif visited[next_x][next_y] and next_y >= 0:
                # 큐에 넣기
                dq.append([[next_x, next_y], cnt+1])
    return 0


# 입력
N, K = map(int, input().strip().split())
data_list = [list(map(int, list(input().strip()))) for _ in range(2)]
print(solution(N, K, data_list))