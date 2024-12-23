import sys

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


def solution(N, M, edges):
    # 피로도가 가장 낮은 그룹 / 피로도
    min_group = list(range(N+1))
    min_fat = 0
    # 정렬 / 낮은 그룹
    min_edges = sorted(edges, key=lambda x:-x[-1])
    # 낮은 그룹 병합
    for a, b, c in min_edges:
        # 낮은
        min_state, min_group = Union(min_group, a, b)
        # 병합 되었으면
        if min_state:
            # 피로도 더해주기
            min_fat += 1-c

    # 피로도가 가장 높은 그룹 / 피로도
    max_group = list(range(N+1))
    max_fat = 0
    # 정렬 / 높은 그룹
    max_edges = sorted(edges, key=lambda x:x[-1])
    # 높은 그룹 병합
    for a, b, c in max_edges:
        # 높은
        max_state, max_group = Union(max_group, a, b)
        # 병합 되었으면
        if max_state:
            # 피로도 더해주기
            max_fat += 1-c
    
    # 빼주기
    print(max_fat**2 - min_fat**2)


# 입력
N, M = map(int, input().strip().split())
edges = [list(map(int, input().strip().split())) for _ in range(M+1)]

solution(N, M, edges)