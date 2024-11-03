import sys

sys.setrecursionlimit(1000)
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


def solution(N, M, idxs, connected):
    # 그룹 리스트
    group_list = list(range(N))
    # 이미 연결된 노드 그룹화
    for a, b in connected:
        Union(a, b, group_list)
    
    # 엣지
    edges = []
    # 가능한 엣지들
    for i in range(len(idxs)-1):
        for j in range(1, len(idxs)):
            edges.append([i, j, pow(pow(idxs[i][0]-idxs[j][0], 2) + pow(idxs[i][1]-idxs[j][1], 2), 1/2)])
    
    edges = sorted(edges, key=lambda x: x[-1])
    # 코스트
    cost = 0
    # 크루스칼
    for a, b, c in edges:
        # 유니온
        state, group_list = Union(a, b, group_list)
        # 연결되었다면
        if state:
            # 코스트 합
            cost += c
    
    print(f'{cost:.2f}')


# 입력
N, M = map(int, input().strip().split())
idxs = [list(map(int, input().strip().split())) for _ in range(N)]
connected = [list(map(lambda x: int(x)-1, input().strip().split())) for _ in range(M)]

solution(N, M, idxs, connected)