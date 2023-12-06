import heapq
import sys


def solution(V, data_list):
    # 트리
    tree = [[] for _ in range(V+1)]
    for data in data_list:
        for idx in range(1, len(data), 2):
            if data[idx] != -1:
                tree[data[0]].append([data[idx], data[idx+1]])
    # 임의의 점에서 다익스트라
    len_list = dijkstra(V, 1, tree)
    # 가장 먼 점 찾기
    rad_node = len_list.index(max(len_list[1:]))
    # 가장 먼 점에서 다익스트라
    len_list = dijkstra(V, rad_node, tree)
    # 지름
    diameter = max(len_list[1:])

    return diameter


# 다익스트라
def dijkstra(V, start, tree):
    # 최대 크기
    inf = float('inf')
    # 거리 리스트
    len_list = [inf for _ in range(V+1)]
    len_list[start] = 0
    # 큐, [가중치, 노드]
    hq = [[0, start]]
    while True:
        # 큐가 비면 끝
        if not hq:
            return len_list
        # 누적 가중치, 노드
        weight, node = heapq.heappop(hq)
        # 가중치가 최소 가중치보다 크면 패스
        if weight > len_list[node]:
            continue
        # 탐색
        for next_node, next_weight in tree[node]:
            # 다음 누적 가중치
            add_weight = weight + next_weight
            # 비교
            if add_weight < len_list[next_node]:
                # 큐에 추가
                heapq.heappush(hq, [add_weight, next_node])
                # 거리 최신화
                len_list[next_node] = add_weight


V = int(sys.stdin.readline())
data_list = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(V)]
print(solution(V, data_list))