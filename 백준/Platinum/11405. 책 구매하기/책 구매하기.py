import sys
from collections import deque

input = sys.stdin.readline


# SPFA
def spfa(start, N, M, graph, flowable):
    # 방문 목록
    visited = [-1 for _ in range(1+M+N+1)]
    visited[start] = start
    # 최단거리
    min_dists = [float('inf') for _ in range(1+M+N+1)]
    min_dists[start] = 0
    # 변한 노드 큐
    changed = deque([start])
    # 변한 횟수
    changed_cnt = [0 for _ in range(1+M+N+1)]
    changed_cnt[start] = 1
    # 순회
    while changed:
        # 현재 노드
        now_node = changed.popleft()
        # 현재 노드가 노드의 수 이상으로 변했으면
        if changed_cnt[now_node] >= 1+M+N+1:
            break

        # 이동 가능한 노드 순회
        for next_node, dist in graph[now_node]:
            # 다음 노드까지 이동 가능한 유체가 남아있으면
            if flowable[now_node][next_node]:
                # 다음 노드까지 이동하는 거리
                next_dist = min_dists[now_node] + dist
                # 다음 노드까지 이동 거리가 최단 거리보다 짧으면
                if next_dist < min_dists[next_node]:
                    # 큐에 추가
                    changed.append(next_node)
                    # 최단거리 갱신
                    min_dists[next_node] = next_dist
                    # 바뀐 횟수 갱신
                    changed_cnt[next_node] += 1
                    # 방문 체크
                    visited[next_node] = now_node

    # 싱크에 도달하지 못하면
    if visited[1+M+N] == -1:
        return []
    
    # 최단 루트
    route = deque([1+M+N])
    # 순회
    while route[0]:
        route.appendleft(visited[route[0]])
    
    return route


def solution(N, M, hope_list, able_list, cost_list):
    # 그래프 / [노드, 코스트] / 소스(1) / 서점(M) / 사람(N) / 싱크(1)
    graph = [[] for _ in range(1+M+N+1)]
    # 흐를 수 있는 유체의 양
    flowable = [[0 for _ in range(1+M+N+1)] for __ in range(1+M+N+1)]
    ### 순회하며 채우기
    ## 그래프
    # 소스 -> 서점
    for b in range(M):
        graph[0].append([1+b, 0])
        graph[1+b].append([0, 0])
    
    # 서점 -> 사람
    for b in range(len(cost_list)):
        for p in range(len(cost_list[b])):
            graph[1+b].append([1+M+p, cost_list[b][p]])
            graph[1+M+p].append([1+b, -cost_list[b][p]])
    
    # 사람 -> 싱크
    for p in range(N):
        graph[1+M+p].append([1+M+N, 0])
        graph[1+M+N].append([1+M+p, 0])

    ## 유체
    # 소스 -> 서점
    for b in range(len(able_list)):
        flowable[0][1+b] = able_list[b]
    
    # 서점 -> 사람
    for p in range(len(hope_list)):
        for b in range(M):
            flowable[1+b][1+M+p] = hope_list[p]
    
    # 사람 -> 싱크
    for p in range(len(hope_list)):
        flowable[1+M+p][1+M+N] = hope_list[p]
    
    # 총 코스트
    total_cost = 0
    # 도달할 수 없을 때 까지 순회
    while True:
        # 루트
        route = spfa(0, N, M, graph, flowable)
        # 도달할 수 없으면 끝
        if not route:
            break
        
        # 루트를 따라 유체 이동
        # 이동시킬 유체
        flow = min([flowable[route[i]][route[i+1]] for i in range(len(route)-1)])
        # 순회
        for i in range(len(route)-1):
            # 유체 이동
            flowable[route[i]][route[i+1]] -= flow
            flowable[route[i+1]][route[i]] += flow
            # 코스트 더해주기
            for j, c in graph[route[i]]:
                if j == route[i+1]:
                    total_cost += c*flow
                    break

    print(total_cost)


# 입력
N, M = map(int, input().strip().split())
hope_list = list(map(int, input().strip().split()))
able_list = list(map(int, input().strip().split()))
cost_list = [list(map(int, input().strip().split())) for _ in range(M)]

solution(N, M, hope_list, able_list, cost_list)