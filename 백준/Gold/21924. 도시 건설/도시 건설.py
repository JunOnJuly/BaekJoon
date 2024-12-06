import sys

input = sys.stdin.readline


# Union-Find
def Union(root_list, node_1, node_2):
    # 각 노드의 루트
    root_node_1 = Find(root_list, node_1)
    root_node_2 = Find(root_list, node_2)
    # 두 노드의 루트가 같으면
    if root_node_1 == root_node_2:
        # 병합하지 않고 루트 리스트 리턴
        return False, root_list
    
    # 두 노드의 루트가 다르면
    else:
        # 루트가 작은쪽으로 병합하고 루트리스트 리턴
        if root_node_1 < root_node_2:
            root_list[root_node_2] = root_list[root_node_1]

        else:
            root_list[root_node_1] = root_list[root_node_2]

        return True, root_list


def Find(root_list, node):
    # 자신의 루트가 자신이 아니라면
    if root_list[node] != node:
        # 거슬러 올라가며 루트 정렬
        root_list[node] = Find(root_list, root_list[node])
    
    return root_list[node]


def solution(N, M, edges):
    # 엣지 정렬
    edges = sorted(edges, key=lambda x: x[-1])
    # 절약되는 코스트
    saved_cost = sum([c for a, b, c in edges])
    # 그룹 리스트
    group_list = list(range(N+1))
    # 노드 개수
    node_cnt = 0
    # 순회
    for a, b, c in edges:
        # 노드 개수가 N-1 이면 끝
        if node_cnt == N-1:
            break

        # 병합
        state, group_list = Union(group_list, a, b)
        # 병합 되었으면
        if state:
            # 코스트 빼주기
            saved_cost -= c
            # 노드 개수 더해주기
            node_cnt += 1
    
    # 모든 건물이 연결되어있으면
    if node_cnt == N-1:
        print(saved_cost)
    
    # 아니면
    else:
        print(-1)


# 입력
N, M = map(int, input().strip().split())
edges = [list(map(int, input().strip().split())) for _ in range(M)]

solution(N, M, edges)