from collections import deque
import heapq
import sys
input = sys.stdin.readline


def solution(n, d, c, dependency_list):
    # BFS, 다익스트라랑 비슷함
    # 트리 / tree[i] = [[i 의 자식 노드, 시간], ...]
    tree = [[] for _ in range(n+1)]
    # 트리 정리
    for a, b, s in dependency_list:
        # 트리 정리
        tree[b].append([a, s])
    # 큐
    queue = [[0, c]]
    # 시스템상 가장 큰 수
    inf = float('INF')
    # 현재 노드까지 감염되는데 걸리는 최단 시간
    time_list = [inf for _ in range(n+1)]
    # 감염된 노드 수
    infected = set([c])
    # 트리 순회
    while queue:
        # 현재 노드, 시간
        now_time, now_node = heapq.heappop(queue)
        # 현재 시간이 최단 시간보다 길면 탐험할 필요 없음
        if time_list[now_node] < now_time:
            continue
        # 자식 탐색
        for node, time in tree[now_node]:
            # 다음 노드까지의 시간이 현재 최단시간보다 길면 탐색할 필요 없음
            if time_list[node] > now_time + time:
                # 최단 시간 최신화
                time_list[node] = now_time + time
                # 큐에 추가
                heapq.heappush(queue, [now_time+time, node])
                # 감염된 노드에 추가
                infected.add(node)
    print(f'{len(infected)} {max([i if i != inf else 0 for i in time_list])}')


T = int(input())
for _ in range(T):
    n, d, c = map(int, input().split())
    dependency_list = [list(map(int, input().strip().split())) for _ in range(d)]
    solution(n, d, c, dependency_list)