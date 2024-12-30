import sys
import heapq as hq

input = sys.stdin.readline


def solution(N, A, B, C, M, edges):
    # 그래프
    graph = [[] for _ in range(N+1)]
    for D, E, L in edges:
        graph[D].append([E, L])
        graph[E].append([D, L])
    
    # 최단거리 리스트
    min_dists = [float('inf') for _ in range(N+1)]
    # 큐
    q = [[0, A], [0, B], [0, C]]
    min_dists[A] = 0
    min_dists[B] = 0
    min_dists[C] = 0
    # 순회
    while q:
        # 현재 거리 / 노드
        now_dist, now_node = hq.heappop(q)
        # 현재 노드의 최소거리보다 길면 패스
        if now_dist > min_dists[now_node]:
            continue

        # 순회
        for next_node, dist in graph[now_node]:
            # 다음 거리
            next_dist = now_dist + dist
            # 다음 거리가 최소거리보다 짧으면
            if next_dist < min_dists[next_node]:
                # 큐에 추가
                hq.heappush(q, [next_dist, next_node])
                # 최단거리 갱신
                min_dists[next_node] = next_dist
    
    # 가장 먼 곳
    max_dist = 0
    max_node = -1
    # 순회
    for node in range(1, N+1):
        # 가장 먼 곳이면 갱신
        if min_dists[node] > max_dist:
            max_dist = min_dists[node]
            max_node = node

    print(max_node)


# 입력
N = int(input().strip())
A, B, C = map(int, input().strip().split())
M = int(input().strip())
edges = [list(map(int, input().strip().split())) for _ in range(M)]

solution(N, A, B, C, M, edges)