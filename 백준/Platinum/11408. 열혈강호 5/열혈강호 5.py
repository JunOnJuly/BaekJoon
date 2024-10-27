import sys
from collections import deque

input = sys.stdin.readline


# SPFA
def spfa(N, M, graph, flowable):
    # 노드 수
    V = N+M+2
    # 직전 노드
    visited = [-1 for _ in range(V)]
    visited[0] = 0
    # 거리가 갱신된 노드들
    dq = deque([0])
    # 데크에 노드가 들어간 수
    in_dq = [0 for _ in range(V)]
    in_dq[0] = 1
    # 최단거리
    min_dists = [float('inf') for _ in range(V)]
    min_dists[0] = 0
    # 순회
    while dq:
        # 현재 노드
        now_node = dq.popleft()
        # 현재 노드가 V 번 이상 데크에 들어갔으면
        if in_dq[now_node] >= V:
            # 음의 순환이 생기면 중단
            break

        # 현재 노드와 연결된 노드 순회
        for next_node, dist in graph[now_node]:
            # 연결된 노드에 흐를수 있는 유체의 양이 남아있으면
            if flowable[now_node][next_node]:
                # 다음 노드까지의 거리
                next_dist = min_dists[now_node] + dist
                # 최단 거리보다 짧으면
                if next_dist < min_dists[next_node]:
                    # 최단 거리 갱신
                    min_dists[next_node] = next_dist
                    # 직전 노드 갱신
                    visited[next_node] = now_node
                    # 데크에 들어가 있지 않으면
                    if next_node not in dq:
                        # 데크에 삽입
                        dq.append(next_node)
                        # 들어간 횟수 추가
                        in_dq[next_node] += 1

    # 마지막에 도달하지 못했으면
    if min_dists[-1] == float('inf'):
        return [], -1
    
    # 최단 경로
    route = deque([V-1])
    while route[0] != 0:
        route.appendleft(visited[route[0]])

    return route, min_dists[-1]


def solution(N, M, edges):
    # 노드의 수
    # 소스 + 노드들 + 싱크
    V = N + M + 2
    # 엣지  정리
    edges = [[[edges[i][j]+N, edges[i][j+1]] for j in range(0, len(edges[i]), 2)] for i in range(len(edges))]
    # 그래프
    graph = [[] for _ in range(V)]
    # 소스 -> 직원
    for i in range(1, N+1):
        graph[0].append([i, 0])
        graph[i].append([0, 0])

    # 직원 -> 일
    for i in range(len(edges)):
        for j, c in edges[i]:
            graph[1+i].append([j, c])
            graph[j].append([1+i, -c])

    # 일 -> 싱크
    for i in range(1+N, 1+N+M):
        graph[i].append([V-1, 0])
        graph[V-1].append([i, 0])
    
    # 흐를수 있는 유체의 양
    flowable = [[0 for _ in range(V)] for __ in range(V)]
    for i in range(len(graph)):
        for j, c in graph[i]:
            # 정방향일때만 
            if i < j:
                flowable[i][j] = 1

    # 총 코스트
    cost_sum = 0
    # 할 수 있는 일
    work_sum = 0
    # 마지막에 도달할 수 없을 때 까지
    while True:
        # 코스트가 최소인 경로, 코스트
        route, cost = spfa(N, M, graph, flowable)
        # 도달할 수 없으면 
        if not route:
            # 끝
            break
        
        # 경로를 따라 유체 이동
        for i in range(len(route)-1):
            flowable[route[i]][route[i+1]] -= 1
            flowable[route[i+1]][route[i]] += 1

        # 코스트 합
        cost_sum += cost
        work_sum += 1
    
    print(work_sum)
    print(cost_sum)


# 입력
N, M = map(int, input().strip().split())
edges = [list(map(int, input().strip().split()[1:])) for _ in range(N)]

solution(N, M, edges)