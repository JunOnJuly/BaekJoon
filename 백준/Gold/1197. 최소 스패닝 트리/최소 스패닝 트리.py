import sys

input = sys.stdin.readline


# 크루스칼 알고리즘을 위한 Union-Find
# Union
def Union(root_list, node_1, node_2):
    # 각 노드의 루트
    root_1 = Find(root_list, node_1)
    root_2 = Find(root_list, node_2)
    # 각 루트가 같으면
    if root_1 == root_2:
        return False
    # 다르면 루트가 작은쪽으로 병합
    else:
        if root_1 > root_2:
            root_list[root_1] = root_list[root_2]
        else:
            root_list[root_2] = root_list[root_1]

    return True


# Find
def Find(root_list, node):
    # 자신의 루트가 자신이 아니면
    if root_list[node] != node:
        # 거슬러 올라가며 탐색
        root_list[node] = Find(root_list, root_list[node])
    
    return root_list[node]


def solution(V, E, edge_list):
    # 가중치가 작은순으로 정렬
    edge_list = sorted(edge_list, key=lambda x: x[-1])
    # Union-Find 를 위한 루트 리스트
    root_list = [i for i in range(V+1)]
    # 최소 코스트
    min_cost = 0
    # 이은 엣지의 수
    edge_cnt = 0
    # 엣지 리스트 순회
    for A, B, C in edge_list:
        # 엣지의 수가 V-1 이면 끝
        if edge_cnt >= V-1:
            break

        # A 노드와 B 노드가 다른 그룹이면 엣지를 추가
        if Union(root_list, A, B):
            min_cost += C
            edge_cnt += 1

    print(min_cost)


# 입력
V, E = map(int, input().strip().split())
edge_list = [list(map(int, input().strip().split())) for _ in range(E)]

solution(V, E, edge_list)