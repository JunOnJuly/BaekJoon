import sys
import heapq as hq

input = sys.stdin.readline


def solution(N, M, K, X, edges):
    # 그래프
    graph = [[] for _ in range(N+1)]
    for A, B in edges:
        graph[A].append(B)

    # 최단거리 목록
    min_dists = [float('inf') for _ in range(N+1)]
    min_dists[X] = 0
    # 큐
    q = [[0, X]]
    # 순회
    while q:
        # 현재 거리 / 도시
        now_dist, now_node = hq.heappop(q)
        # 현재 거리가 최단거리보다 길면
        if now_dist > min_dists[now_node]:
            continue
            
        # 이동 가능 노드 순회
        for next_node in graph[now_node]:
            # 다음 거리
            next_dist = now_dist + 1
            # 다음 거리가 최단거리보다 짧으면
            if next_dist < min_dists[next_node]:
                # 최단거리 갱신
                min_dists[next_node] = next_dist
                # 큐에 추가
                hq.heappush(q, [next_dist, next_node])
    
    # 카운트
    cnt = 0
    # 순회 및 출력
    for i in range(1, len(min_dists)):
        if min_dists[i] == K:
            cnt += 1
            print(i)
    
    if not cnt:
        print(-1)


# 입력
N, M, K, X = map(int, input().strip().split())
edges = [list(map(int, input().strip().split())) for _ in range(M)]

solution(N, M, K, X, edges)