import sys
from collections import deque

input = sys.stdin.readline


def solution(N, time_list, topol_list, graph):
    # 큐
    dq = deque([])
    # 방문 기록
    visited = [False for _ in range(N+1)]
    # 필요한 시간 리스트
    max_times = [0 for _ in range(N+1)]
    # 시작 노드 찾기
    # 선행 노드가 없는 노드
    for i in range(1, len(topol_list)):
        if not topol_list[i]:
            # 큐에 추가
            dq.append([i, 0])
    # 순회
    while dq:
        # 현재 인덱스, 현재까지 걸리는 시간
        now_idx, now_time = dq.popleft()
        # 방문 체크
        visited[now_idx] = True
        # 현재 인덱스에서 이동 가능한 인덱스 순회
        for next_idx in graph[now_idx]:
            # 최대 도달 시간 체크
            max_times[next_idx] = max(max_times[next_idx], now_time + time_list[now_idx])
            # 선행 노드를 모두 방문했으면
            if all([visited[topol] for topol in topol_list[next_idx]]):
                # 최대 도달 시간 넣기
                dq.append([next_idx, max_times[next_idx]])
    
    # 자신을 짓는 시간 더해주기
    for i in range(len(visited)):
        max_times[i] += time_list[i]

    return max_times[1:]


# 입력
N = int(input().strip())
topol_list = [[]]
time_list = [0]
graph = [[] for _ in range(N+1)]
for i in range(N):
    data = list(map(int, input().strip().split()))
    time_list.append(data[0])
    topol_list.append(data[1:-1])
    for topol in topol_list[i+1]:
        graph[topol].append(i+1)

for time in solution(N, time_list, topol_list, graph):
     print(time)