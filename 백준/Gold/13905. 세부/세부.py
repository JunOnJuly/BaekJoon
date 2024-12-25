import sys
from collections import deque

input = sys.stdin.readline


## Union-Find

# Find
def Find(group_list, node):
    # 루트 노드가 아니면
    if group_list[node] != node:
        group_list[node] = Find(group_list, group_list[node])
    
    return group_list[node]


# Union
def Union(group_list, n1, n2):
    # 그룹
    g1 = Find(group_list, n1)
    g2 = Find(group_list, n2)
    # 같은 그룹이면
    if g1 == g2:
        # 병합하지 않음
        return False, group_list

    # 작은 쪽으로 병합
    if g1 < g2:
        group_list[g2] = g1
    
    else:
        group_list[g1] = g2

    return True, group_list


def solution(N, M, s, e, edges):
    # 다리를 무게 제한을 기준으로 내림차순 정렬
    edges.sort(key=lambda x: -x[-1])
    # 그룹 리스트
    group_list = list(range(N+1))
    # 연결된 엣지
    connected_edges = [[] for _ in range(N+1)]
    # 순회
    for h1, h2, k in edges:
        # 병합
        state, group_list = Union(group_list, h1, h2)
        # 병합 되었으면
        if state:
            # 연결된 엣지 추가
            connected_edges[h1].append([h2, k])
            connected_edges[h2].append([h1, k])
            # 출발 - 목적 위치가 연결되었으면 중단
            if Find(group_list, s) == Find(group_list, e):
                break
    
    ## 연결된 노드를 탐색하며 출발 - 목적 경로 탐색
    # 데크 / [현재 노드, 들고있는 빼빼로 수]
    dq = deque([[s, float('inf')]])
    # 방문 목록
    visited = [1 for _ in range(N+1)]
    visited[s] = 0
    # 순회
    while dq:
        # 현재 노드 / 들고있는 빼빼로 수
        now_node, got_ppr = dq.popleft()
        # 현재 노드가 목적 노드면
        if now_node == e:
            # 들고 있는 빼뺴로 출력
            print(got_ppr)
            return 
        
        # 이동 가능한 노드 순회
        for next_node, cost in connected_edges[now_node]:
            # 방문하지 않았으면
            if visited[next_node]:
                # 방문 체크
                visited[next_node] = 0
                # 데크에 추가
                dq.append([next_node, min(got_ppr, cost)])

    print(0)
    

# 입력
N, M = map(int, input().strip().split())
s, e = map(int, input().strip().split())
edges = [list(map(int, input().strip().split())) for _ in range(M)]

solution(N, M, s, e, edges)