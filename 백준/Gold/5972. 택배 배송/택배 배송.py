import sys
import heapq as hq
from collections import deque

input = sys.stdin.readline


def solution(N, M, edges):
    # 그래프
    graph = [[] for _ in range(N+1)]
    for a, b, c in edges:
        graph[a].append([b, c])
        graph[b].append([a, c])

    # 최단여물
    min_feeds = [float('inf') for _ in range(N+1)]
    min_feeds[1] = 0
    # 큐
    q = [[0, 1]]
    # 순회
    while q:
        # 현재 여물 / 현재 노드
        now_feed, now_node = hq.heappop(q)
        # 현재 여물이 현재 노드에서 최소 여물보다 많으면 패스
        if now_feed > min_feeds[now_node]:
            continue
            
        # 순회
        for next_node, feed in graph[now_node]:
            # 다음 노드까지 여물
            next_feed = now_feed + feed
            # 다음 여물이 다음 노드까지의 최단거리보다 적으면
            if next_feed < min_feeds[next_node]:
                # 최단거리 갱신
                min_feeds[next_node] = next_feed
                # 큐에 넣기
                hq.heappush(q, [next_feed, next_node])
    
    print(min_feeds[N])


# 입력
N, M = map(int, input().strip().split())
edges = [list(map(int, input().strip().split())) for _ in range(M)]

solution(N, M, edges)