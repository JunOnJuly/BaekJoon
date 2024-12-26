import sys
import heapq as hq

input = sys.stdin.readline


def solution(n, m, k, edges):
    # 그래프 정리
    graph = [[] for _ in range(n+1)]
    for a, b, c in edges:
        graph[a].append([b, c])
    
    # 큐
    q = [[0, 1]]
    # k 번째 최단시간
    kth_min_dists = [[] for _ in range(n+1)]
    kth_min_dists[1].append(0)
    # 순회
    while q:
        # 소요 시간 / 현재 도시
        now_time, now_node = hq.heappop(q)
        # 순회
        for next_node, time in graph[now_node]:
            # 다음 노드까지 시간
            next_time = now_time + time
            # 다음 노드의 최단 시간 후보
            nn_kth_nodes = kth_min_dists[next_node]
            # 해당 노드까지 최단 시간 후보가 k 개 이하면
            if len(nn_kth_nodes) < k:
                # 후보에 넣어주기
                hq.heappush(kth_min_dists[next_node], -next_time)
                # 큐에 추가
                hq.heappush(q, [next_time, next_node])
            
            # k 개 존재하고 현재 k 번째 최단 시간보다 빠르면
            elif len(nn_kth_nodes) == k and next_time < -nn_kth_nodes[0]:
                # 후보 팝
                hq.heappop(kth_min_dists[next_node])
                # 후보에 넣어주기
                hq.heappush(kth_min_dists[next_node], -next_time)
                # 큐에 추가
                hq.heappush(q, [next_time, next_node])
    
    for i in range(1, n+1):
        # k 번째 후보가 존재하면
        if len(kth_min_dists[i]) == k:
            print(-kth_min_dists[i][0])
        
        else:
            print(-1)
    

# 입력
n, m, k = map(int, input().strip().split())
edges = [list(map(int, input().strip().split())) for _ in range(m)]

solution(n, m, k, edges)