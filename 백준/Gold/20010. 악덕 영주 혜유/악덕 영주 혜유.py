import sys
from collections import deque as dq

input = sys.stdin.readline


## Union-Find

# Find
def Find(group_list, node):
    # 자신이 그룹의 대표가 아니면
    if group_list[node] != node:
        # 재귀적으로 재탐색
        group_list[node] = Find(group_list, group_list[node])
    
    return group_list[node]


# Union
def Union(group_list, n1, n2):
    # 그룹
    g1 = Find(group_list, n1)
    g2 = Find(group_list, n2)
    # 그룹이 같으면
    if g1 == g2:
        # 병합하지 않음
        return False, group_list

    # 그룹이 작은 쪽으로 병합
    if g1 < g2:
        group_list[g2] = g1
    
    else:
        group_list[g1] = g2
    
    return True, group_list


def solution(N, K, edges):
    # 엣지 정렬
    edges = sorted(edges, key=lambda x:x[-1])
    # 그룹 리스트
    group_list = list(range(N+1))
    # 최소 스패닝 트리 그래프
    mst_graph = [[] for _ in range(N)]
    # 최소 스패닝 트리 비용
    mst_cost = 0
    # 순회
    for a, b, c in edges:
        # 병합
        state, group_list = Union(group_list, a, b)
        # 병합 되었으면
        if state:
            # 비용 더해주기
            mst_cost += c
            # 트리 그래프 갱신
            mst_graph[a].append([b, c])
            mst_graph[b].append([a, c])

    # 임의의 시작 노드
    s = 0
    for _ in range(2):
        # 노드 순회
        dists = [-1 for _ in range(N)]
        dists[s] = 0
        # 큐
        q = dq([[s, 0]])
        # 최대 거리
        max_dist = 0
        # 최대 거리 노드
        max_dist_node = 0
        # DFS
        while q:
            # 현재 노드 / 현재 거리
            now_node, now_dist = q.popleft()
            # 이동 가능 노드 순회
            for next_node, dist in mst_graph[now_node]:
                # 다음 노드까지 거리가 기록되지 않았을때만
                if dists[next_node] < 0:
                    # 다음 노드까지 거리
                    next_dist = now_dist + dist
                    # 큐에 추가
                    q.append([next_node, next_dist])
                    # 거리 최신화
                    dists[next_node] = next_dist
                    # 최대거리 갱신
                    if next_dist > max_dist:
                        max_dist = next_dist
                        max_dist_node = next_node
                        # 시작 노드 변경
                        s = max_dist_node
    
    print(mst_cost)
    print(max_dist)


# 입력
N, K = map(int, input().strip().split())
edges = [list(map(int, input().strip().split())) for _ in range(K)]

solution(N, K, edges)