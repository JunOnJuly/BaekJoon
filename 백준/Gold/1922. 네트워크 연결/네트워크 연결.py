import sys

input = sys.stdin.readline


# Union-Find
def Union(root_list, node_1, node_2):
    # 각 루트 노드
    root_1 = Find(root_list,node_1)
    root_2 = Find(root_list, node_2)
    # 루트 노드가 같으면
    if root_1 == root_2:
        return False, root_list
    # 루트 노드가 다르면
    else:
        # root_1 에 맞추기
        root_list[root_2] = root_list[root_1]
        return True, root_list


def Find(root_list, node):
    # 자신의 루트가 자신이 아니면
    if root_list[node] != node:
        root_list[node] = Find(root_list, root_list[node])

    return root_list[node]


def solution(N, M, edges):
    # Union-Find 알고리즘을 위한 루트리스트
    # 자신의 루트는 자신
    root_list = list(range(N+1))

    ## 크루스칼 알고리즘
    # 엣지를 코스트가 작은순으로 정렬
    edges.sort(key=lambda x: x[2])

    # 코스트
    cost = 0
    # 엣지를 순회
    for n1, n2, c in edges:
        # 두 노드의 루트가 같지 않으면 이어주기 (순환노드가 아니면)
        state, root_list = Union(root_list, n1, n2)
        # 코스트 더해주기
        if state:
            cost += c
    
    return cost


# 입력
N = int(input().strip())
M = int(input().strip())
edges = [list(map(int, input().strip().split())) for _ in range(M)]

print(solution(N, M, edges))