import sys
import heapq as hq

input = sys.stdin.readline


# 다익스트라
def dijkstra(graph, stores):
    # 큐
    q = [[0, store] for store in stores]
    # 최단거리 리스트
    min_dists = [float('inf') for _ in range(len(graph))]
    for store in stores:
        min_dists[store] = 0

    # 순회
    while q:
        # 거리 / 노드
        now_dist, now_node = hq.heappop(q)
        # 현재 거리가 현재 노드의 최단거리보다 길면 패스
        if now_dist > min_dists[now_node]:
            continue

        # 이동 가능 노드 탐색
        for next_node, dist in graph[now_node]:
            # 다음 거리
            next_dist = now_dist + dist
            # 다음 거리가 다음 노드의 최단거리보다 짧을때만
            if next_dist < min_dists[next_node]:
                # 큐에 추가
                hq.heappush(q, [next_dist, next_node])
                # 최단거리 갱신
                min_dists[next_node] = next_dist
    
    return min_dists


def solution(V, E, edges, M, x, Ms, S, y, Ss):
    # 그래프
    graph = [[] for _ in range(V+1)]
    for u, v, w in edges:
        graph[u].append([v, w])
        graph[v].append([u, w])
    
    # 모든 가게부터 가게가 없는 위치까지의 거리 구하기
    M_dists = dijkstra(graph, Ms)
    S_dists = dijkstra(graph, Ss)
    # 조건에 맞는 노드 찾기
    min_dist = float('inf')
    for m, s in zip(M_dists, S_dists):
        # 가게 위치가 아니고 범위 안에 있으면
        if (m and m <= x) and (s and s <= y):
            # 최단거리 갱신
            min_dist = min(min_dist, m+s)

    print(min_dist if min_dist != float('inf') else -1)


# 입력
V, E = map(int, input().strip().split())
edges = [list(map(int, input().strip().split())) for _ in range(E)]
M, x = map(int, input().strip().split())
Ms = list(map(int, input().strip().split()))
S, y = map(int, input().strip().split())
Ss = list(map(int, input().strip().split()))

solution(V, E, edges, M, x, Ms, S, y, Ss)