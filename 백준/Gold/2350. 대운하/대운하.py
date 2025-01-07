import sys
from collections import deque

input = sys.stdin.readline


# union-find
def Union(group_list, n1, n2):
    # 그룹
    g1 = Find(group_list, n1)
    g2 = Find(group_list, n2)
    # 두 그룹이 같으면
    if g1 == g2:
        # 병합하지 않음
        return False, group_list
    
    # 다르면 그룹이 작은쪽으로 병합
    if g1 > g2:
        group_list[g1] = g2
    
    else:
        group_list[g2] = g1
    
    return True, group_list


def Find(group_list, n):
    # 자신이 그룹의 대표가 아니면
    if group_list[n] != n:
        # 재귀적으로 업데이트
        group_list[n] = Find(group_list, group_list[n])
    
    return group_list[n]


def solution(N, M, K, edges, targets):
    # 엣지 내림차순 정렬
    edges = sorted(edges, key=lambda x: x[-1], reverse=True)
    # 그룹 리스트
    group_list = list(range(N+1))
    # 그래프
    graph = [[] for _ in range(N+1)]
    # 순회
    for i, j, w in edges:
        # 병합
        state, group_list = Union(group_list, i, j)
        # 병합되었으면
        if state:
            # 그래프에 추가
            graph[i].append([j, w])
            graph[j].append([i, w])
    
    # 타겟 순회
    for i, j in targets:
        # 큐
        dq = deque([[i, float('inf')]])
        # 방문 목록
        visited = [1 for _ in range(N+1)]
        # 순회
        while dq:
            # 노드 / 최대비용
            now_node, max_cost = dq.popleft()
            # 노드가 목표 노드면
            if now_node == j:
                print(max_cost)
                break

            # 연결된 노드 탐색
            for next_node, cost in graph[now_node]:
                # 방문하지 않았으면
                if visited[next_node]:
                    # 방문
                    visited[next_node] = 0
                    # 큐에 넣기
                    dq.append([next_node, min(max_cost, cost)])


# 입력
N, M, K = map(int, input().strip().split())
edges = [list(map(int, input().strip().split())) for _ in range(M)]
targets = [list(map(int, input().strip().split())) for _ in range(K)]

solution(N, M, K, edges, targets)