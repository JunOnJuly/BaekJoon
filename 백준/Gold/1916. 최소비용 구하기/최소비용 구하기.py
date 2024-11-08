import sys
import heapq

input = sys.stdin.readline


def solution(N, M, edges, s, e):
    ## 다익스트라
    # 그래프
    graph = [[] for _ in range(N+1)]
    for a, b, c in edges:
        graph[a].append([b, c])
    
    # 최소 비용
    min_cost = [float('inf') for _ in range(N+1)]
    min_cost[s] = 0
    # 큐
    q = [[0, s]]
    # 순회
    while q:
        # 현재 비용 / 도시
        now_cost, now_node = heapq.heappop(q)
        # 현재 비용이 최소 비용보다 크면
        if now_cost > min_cost[now_node]:
            # 패스
            continue

        # 순회
        for next_node, cost in graph[now_node]:
            # 다음 도시까지 비용
            next_cost = now_cost + cost
            # 최소 비용보다 작으면
            if next_cost < min_cost[next_node]:
                # 목표 노드가 아니면
                if next_node != e:
                    # 큐에 추가
                    heapq.heappush(q, [next_cost, next_node])

                # 최소 비용 갱신
                min_cost[next_node] = next_cost
    
    print(min_cost[e])


# 입력
N = int(input().strip())
M = int(input().strip())
edges = [list(map(int, input().strip().split())) for _ in range(M)]
s, e = map(int, input().strip().split())

solution(N, M, edges, s, e)