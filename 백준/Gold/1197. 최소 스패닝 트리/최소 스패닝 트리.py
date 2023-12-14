import sys
import heapq


def solution(V, E, data_list):
    # kruskal
    weight_sum, tree, union_list = kruskal(V, E, data_list)
    print(weight_sum)


# kruskal
def kruskal(V, E, data_list):
    # 트리, tree[i] = [i번째 노드의 자식들]
    tree = [[] for _ in range(V+1)]
    # 유니온 리스트
    union_list = list(range(V+1))
    # 큐
    queue = []
    # 데이터를 큐에 삽입
    for parent, child, weight in data_list:
        heapq.heappush(queue, [weight, parent, child])
    # 가중치 합
    weight_sum = 0
    # 데이터를 순회하며 트리 완성
    while True:
        # 큐가 비면 끝
        if not queue:
            return weight_sum, tree, union_list
        # 현재 노드, 부모노드, 자식노드
        weight, parent, child = heapq.heappop(queue)
        # 부모와 자식 노드가 순환이 아니면 union
        state, union_list = union(union_list, parent, child)
        # 병합 되었으면 트리에 추가
        if state:
            tree[parent].append(child)
            weight_sum += weight


# union-find
def find(union_list, node):
    # 자신의 루트가 자신이면 리턴
    if union_list[node] == node:
        return node
    # 아니면 순서대로 루트를 바꿔가며 루트의 루트를 반환
    else:
        union_list[node] = find(union_list, union_list[node])
    return union_list[node]


def union(union_list, node_1, node_2):
    # 루트 찾기
    root_1 = find(union_list, node_1)
    root_2 = find(union_list, node_2)
    # 둘의 루트가 같으면
    if root_1 == root_2:
        # 순환이므로 리턴
        return False, union_list
    # 다르면
    else:
        # 루트를 병합
        union_list[root_2] = root_1
        # 리턴
        return True, union_list


V, E = map(int, sys.stdin.readline().strip().split())
data_list = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(E)]
solution(V, E, data_list)