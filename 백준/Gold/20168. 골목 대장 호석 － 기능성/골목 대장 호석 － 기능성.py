import sys
import heapq as hq

input = sys.stdin.readline


def solution(N, M, A, B, C, edges):
    # 그래프 정리
    graph = [[] for _ in range(N+1)]
    for a, b, c in edges:
        graph[a].append([b, c])
        graph[b].append([a, c])
    
    # 큐
    q = [[0, A, 0]]
    # 최소 코스트 리스트
    min_cost = [float('inf') for _ in range(N+1)]
    min_cost[A] = 0
    # 순회
    while q:
        # 최대 코스트 / 현재 노드 / 현재 소모한 돈
        max_cost, now_node, now_cost_money = hq.heappop(q)
        # 최소 코스트보다 코스트가 크면
        if max_cost > min_cost[now_node]:
            continue

        # 순회
        for next_node, cost in graph[now_node]:
            # 다음 노드까지 소모할 돈
            next_cost_money = now_cost_money + cost
            # 다음 노드까지 최대 코스트
            next_max_cost = max(max_cost, cost)
            # 다음 노드까지 최대 코스트가 다음 노드까지 최소 코스트보다 적을때만
            if next_max_cost < min_cost[next_node]:
                # 다음 노드까지 소모할 돈이 예산 범위 안에 있을때만
                if next_cost_money <= C:
                    # 큐에 추가
                    hq.heappush(q, [next_max_cost, next_node, next_cost_money])
                    # 최소 코스트 목록
                    min_cost[next_node] = next_max_cost
    
    print(min_cost[B] if min_cost[B] != float('inf') else -1)


# 입력
N, M, A, B, C = map(int, input().strip().split())
edges = [list(map(int, input().strip().split())) for _ in range(M)]

solution(N, M, A, B, C, edges)