import sys
from collections import deque

def solution(N, M, data_list):
    # 트리
    tree = [[] for _ in range(N+1)]
    for start, end, time in data_list:
        tree[start].append([end, time])
    # 최대 시간
    inf = float('inf')
    # 걸리는 시간 리스트
    time_list = [inf for _ in range(N+1)]
    time_list[1] = 0
    # 벨만-포드
    # 탐색 시작 노드
    for start_node in range(0, N):
        # 현재 탐색 노드
        for now_node in range(start_node, start_node+N):
            # 다음 노드
            # 탐색 시작 노드부터 순환, [1, 2, 3] -> [2, 3, 1] -> [3, 1, 2] 식으로
            for next_node, time in tree[now_node%N + 1]:
                # 다음 노드까지의 시간이 최단시간보다 짧으면 갱신
                if time_list[now_node%N + 1] + time < time_list[next_node]:
                    time_list[next_node] = time_list[now_node%N + 1] + time
    # 음의 루프가 있는지 확인
    for start_node in range(0, N):
        # 현재 탐색 노드
        for now_node in range(start_node, start_node+N):
            # 다음 노드
            # 탐색 시작 노드부터 순환, [1, 2, 3] -> [2, 3, 1] -> [3, 1, 2] 식으로
            for next_node, time in tree[now_node%N + 1]:
                # 다음 노드까지의 시간이 최단시간보다 음의 루프
                if time_list[now_node%N + 1] + time < time_list[next_node]:
                    print(-1)
                    return
    # 음의 루프가 없으면 순서대로 출력
    print(*[time if time != inf else -1 for time in time_list[2:]])


N, M = map(int, sys.stdin.readline().strip().split())
data_list = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(M)]
solution(N, M, data_list)