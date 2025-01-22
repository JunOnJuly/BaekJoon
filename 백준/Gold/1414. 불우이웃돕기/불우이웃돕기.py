import sys

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


def solution(N, edges):
    # 엣지 정리
    edges = [[i, j, ord(edges[i][j]) - ord('a') + 1] if edges[i][j].islower() else 
            [i, j, ord(edges[i][j]) - ord('A') + 27]
            for i in range(N) for j in range(N) if edges[i][j] != '0']

    # 엣지 정렬
    edges = sorted(edges, key=lambda x:x[-1])
    # 그룹 리스트
    group_list = list(range(N))
    # 연결된 길이
    connected_len = 0
    # 연결된 엣지 수
    connected_edges = 0
    # 병합
    for i, j, l in edges:
        # 병합
        state, group_list = Union(i, j, group_list)
        # 병합 되었으면
        if state:
            # 연결된 길이 + l
            connected_len += l
            # 연결된 엣지 + 1
            connected_edges += 1
    
    # 모든 컴퓨터가 연결되었으면
    if connected_edges == N-1:
        print(sum([l for i, j, l in edges]) - connected_len)
    
    # 아니면
    else:
        print(-1)
    

# 입력
N = int(input().strip())
edges = [list(input().strip()) for _ in range(N)]

solution(N, edges)