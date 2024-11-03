import sys

sys.setrecursionlimit(10000)
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


def solution(N, idxs):
    # 엣지 정리
    edges = []
    # x y z 로 각 정렬해 인접한 점들만 탐색
    for key in range(3):
        # 정렬된 좌표
        s_idxs = sorted(idxs, key=lambda x: x[key])
        for i in range(N-1):
            edges.append([s_idxs[i][-1], s_idxs[i+1][-1], min([abs(a-b) for a, b in zip(s_idxs[i][:3], s_idxs[i+1][:3])])])

    edges = sorted(edges, key=lambda x: x[-1])
    # 그룹 리스트
    group_list = list(range(N))
    # 코스트
    cost = 0
    # 크루스칼
    for a, b, c in edges:
        # 유니온
        state, group_list = Union(a, b, group_list)
        # 연결되었으면 코스트 더해주기
        if state:
            cost += c
    
    print(cost)


# 입력
N = int(input().strip())
idxs = [list(map(int, input().strip().split())) + [i] for i in range(N)]

solution(N, idxs)