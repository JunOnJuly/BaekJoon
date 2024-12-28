import sys
import heapq as hq

input = sys.stdin.readline


# 다익스트라
def dijkstra(graph, s, e, b=None):
    # 큐
    q = [[0, s]]
    # 최단거리 리스트
    min_dists = [float('inf') for _ in range(N+1)]
    min_dists[s] = 0
    # 순회
    while q:
        # 거리 / 노드
        now_dist, now_node = hq.heappop(q)
        # 현재 거리가 현재 노드의 최단거리보다 길면 패스
        if now_dist > min_dists[now_node]:
            continue

        # 이동 가능 노드 탐색
        for next_node, dist in graph[now_node]:
            # y 는 거치지 않음
            if b and next_node == b:
                continue
            
            # 다음 거리
            next_dist = now_dist + dist
            # 다음 거리가 다음 노드의 최단거리보다 짧을때만
            if next_dist < min_dists[next_node]:
                # 큐에 추가
                hq.heappush(q, [next_dist, next_node])
                # 최단거리 갱신
                min_dists[next_node] = next_dist
    
    return min_dists[e]


def solution(N, M, edges, x, y, z):
    # 그래프
    graph = [[] for _ in range(N+1)]
    for u, v, w in edges:
        graph[u].append([v, w])

    # x - y - z
    xy = dijkstra(graph, x, y)
    yz = dijkstra(graph, y, z)
    # x - z
    xz = dijkstra(graph, x, z, y)
    
    print(f'{xy + yz if xy + yz != float("inf") else -1} {xz if xz != float("inf") else -1}')
    

# 입력
N, M = map(int, input().strip().split())
edges = [list(map(int, input().strip().split())) for _ in range(M)]
x, y, z = map(int, input().strip().split())

solution(N, M, edges, x, y, z)