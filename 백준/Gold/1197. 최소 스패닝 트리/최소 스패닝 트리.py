import sys

sys.setrecursionlimit(100000)
input = sys.stdin.readline


## Union-Find
# Union
def Union(node1, node2, group_list):
    # 각 노드의 그룹
    group1 = Find(node1, group_list)
    group2 = Find(node2, group_list)
    # 두 그룹이 같으면
    if group1 == group2:
        # 병합하지 않음
        return False, group_list
    
    # 두 그룹이 다르면
    # 작은 쪽으로 병합
    if group1 > group2:
        group_list[group1] = group2
    
    else:
        group_list[group2] = group1
    
    return True, group_list


# Find
def Find(node, group_list):
    # 그룹의 대표가 자신이 아니면
    if group_list[node] != node:
        # 재귀적으로 업데이트
        group_list[node] = Find(group_list[node], group_list)
    
    return group_list[node]


def solution(V, E, edges):
    # 크루스칼
    # 엣지 정렬
    edges = sorted(edges, key=lambda x: x[-1])
    # 그룹 리스트
    group_list = list(range(V+1))
    # 가중치
    cost = 0
    # 엣지 순회
    for A, B, C in edges:
        # 병합
        state, group_list = Union(A, B, group_list)
        # 병합했으면
        if state:
            # 가중치 합
            cost += C
    
    print(cost)


# 입력
V, E = map(int, input().strip().split())
edges = [list(map(int, input().strip().split())) for _ in range(E)]

solution(V, E, edges)