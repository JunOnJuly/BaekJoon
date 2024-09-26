import sys
from collections import deque
import heapq

input = sys.stdin.readline


# 다익스트라
def dijkstra(N, M, i, j, data_map, min_dist_map):
    # 직전 노드 기록
    before_node = [0 for _ in range(N+1)]
    # 최단거리 리스트
    min_dists = [float('inf') for _ in range(N+1)]
    min_dists[i] = 0
    # 힙
    hq = [[0, i]]
    # 순회
    while hq:
        # 현재 이동 거리 / 현재 노드
        now_dist, now_node = heapq.heappop(hq)
        # 현재 노드가 목표 노드면
        if now_node == j:
            break
        # 현재 이동 거리가 최단거리보다 길면
        if now_dist > min_dists[now_node]:
            # 다음으로
            continue
        # 현재 노드에서 이동 가능한 노드 순회
        for dist, next_node in data_map[now_node]:
            # 다음 노드까지 이동 거리
            next_dist = now_dist + dist
            # 다음 노드까지 이동 거리가 다음 노드까지의 최단거리보다 짧으면
            if next_dist < min_dists[next_node]:
                # 직전 노드 기록
                before_node[next_node] = now_node
                # 최단거리 기록
                min_dists[next_node] = next_dist
                # 데크에 삽입
                heapq.heappush(hq, [next_dist, next_node])
    
    # 직전 노드 기록 순회하며 최단이동 경로 파악
    min_move_dq = deque([j])
    while True:
        # 직전 노드
        before = before_node[min_move_dq[0]]
        # 직전 노드가 0 이면 끝
        if not before:
            break
        min_move_dq.appendleft(before)
    
    # 최단경로 안에 있는 노드들은 모두 최선의 경로로 이동했으므로
    # 각각의 최단경로이기도 함
    for i in range(len(min_move_dq)-1):
        for j in range(i+1, len(min_move_dq)):
            min_dist_map[min_move_dq[i]][min_move_dq[j]] = min_move_dq[i+1]
            min_dist_map[min_move_dq[j]][min_move_dq[i]] = min_move_dq[j-1]

    return min_dist_map


def solution(N, M, edges):
    # 노드 목록
    data_map = [[] for _ in range(N+1)]
    for n1, n2, c in edges:
        data_map[n1].append([c, n2])
        data_map[n2].append([c, n1])

    # 최단경로 맵
    min_dist_map = [[float('inf') for _ in range(N+1)] for __ in range(N+1)]
    
    # 최단경로 맵에 등록되어있지 않으면 다익스트라
    # 직접적으로 이어지지 않은 노드 먼저 순회
    
    for i in range(1, N+1):
        for j in range(1, N+1):
            if i != j and min_dist_map[i][j] == float('inf'):
                min_dist_map = dijkstra(N, M, i, j, data_map, min_dist_map)
    
    for i in range(N+1):
        min_dist_map[i][i] = '-'
    
    for i in range(1, len(min_dist_map)):
        print(*min_dist_map[i][1:])


# 입력
N, M = map(int, input().strip().split())
edges = [list(map(int, input().strip().split())) for _ in range(M)]

solution(N, M, edges)