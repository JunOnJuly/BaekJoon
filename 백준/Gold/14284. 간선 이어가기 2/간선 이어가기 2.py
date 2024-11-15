import sys
import heapq

input = sys.stdin.readline


def solution(n, m, edges, s, t):
    # 그래프
    graph = [[] for _ in range(n+1)]
    for a, b, c in edges:
        graph[a].append([b, c])
        graph[b].append([a, c])

    # 최소 가중치 리스트
    min_weights = [float('inf') for _ in range(n+1)]
    # 큐
    hq = [[0, s]]
    # 순회
    while hq:
        # 현재 가중치 / 노드
        now_weight, now_node = heapq.heappop(hq)
        # 현재 가중치가 최소 가중치보다 크면 패스
        if now_weight > min_weights[now_node]:
            continue

        # 이동 가능 노드 순회
        for next_node, weight in graph[now_node]:
            # 다음 가중치
            next_weight = now_weight + weight
            # 다음 가중치가 최소 가중치보다 작으면
            if next_weight < min_weights[next_node]:
                # 큐에 추가
                heapq.heappush(hq, [next_weight, next_node])
                # 최소 가중치 업데이트
                min_weights[next_node] = next_weight
    
    print(min_weights[t])
    

# 입력
n, m = map(int, input().strip().split())
edges = [list(map(int, input().strip().split())) for _ in range(m)]
s, t = map(int, input().strip().split())

solution(n, m, edges, s, t)