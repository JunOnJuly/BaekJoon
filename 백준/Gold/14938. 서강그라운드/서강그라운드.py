import sys

input = sys.stdin.readline


def solution(n, m, r, items, edges):
    ## 플로이드-워셜
    # 최단거리 리스트
    min_dists = [[float('inf') for _ in range(n+1)] for __ in range(n+1)]
    for i in range(n+1):
        min_dists[i][i] = 0
    
    for a, b, l in edges:
        min_dists[a][b] = min(min_dists[a][b], l)
        min_dists[b][a] = min(min_dists[b][a], l)
    
    # 중간 노드
    for mid in range(1, n+1):
        # 출발 노드
        for front in range(1, n+1):
            # 도착 노드
            for back in range(1, n+1):
                # 갱신
                min_dists[front][back] = min(min_dists[front][back], min_dists[front][mid] + min_dists[mid][back])
    
    ## 각 지역에서 도달할 수 있는 지역들 / 아이템 합 찾기
    # 도달할 수 있는 지역
    reachable_nodes = [[j for j in range(1, len(min_dists[i])) if min_dists[i][j] <= m] for i in range(1, n+1) ]
    # 아이템 합
    sum_items = [sum(items[node] for node in reachable_node) for reachable_node in reachable_nodes]
    
    print(max(sum_items))


# 입력
n, m, r = map(int, input().strip().split())
items = [0] + list(map(int, input().strip().split()))
edges = [list(map(int, input().strip().split())) for _ in range(r)]

solution(n, m, r, items, edges)