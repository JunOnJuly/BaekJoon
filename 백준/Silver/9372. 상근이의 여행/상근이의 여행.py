from collections import deque


def solution(N, M, data_list):
    # 프림과 크루스칼 모두 해보자
    # 유니온 리스트
    union_list = list(range(N+1))
    # 크루스칼 / 프림 / N-1 셋 중 하나
    print(kruskal_or_prim_or_none('kruskal', N, M, union_list, data_list))
    print(kruskal_or_prim_or_none('prim', N, M, union_list, data_list))
    print(kruskal_or_prim_or_none('none', N, M, union_list, data_list))


# 크루스칼 프림 선택
# kruskal, prim, none
def kruskal_or_prim_or_none(mode, N, M, union_list, data_list):
    if mode == 'kruskal':
        return kruskal(N, M, union_list, data_list)
    elif mode == 'prim':
        return prim(N, M, union_list, data_list)
    else:
        return N-1


# 유니온 파인드
def union_find(num_1, num_2, union_list):


    # 파인드
    def find(num, union_list):
        # 자신의 부모 노드가 자신이면 끝
        if union_list[num] == num:
            return num
        # 아니면 부모노드 최신화 및 재귀
        else:
            union_list[num] = find(union_list[num], union_list)
        # 유니온 리스트 반환
        return union_list[num]
    

    # 유니온
    def union(num_1, num_2, union_list):
        # 루트 노드
        root_1 = find(num_1, union_list)
        root_2 = find(num_2, union_list)
        # 순환 여부
        state = True
        # 둘이 다르면 순환이 아니므로 합침
        if root_1 != root_2:
            union_list[root_2] = root_1
            state = False
        return state, union_list

    
    return union(num_1, num_2, union_list)


# 크루스칼
def kruskal(N, M, union_list, data_list):
    # 트리, tree[parent] = childs
    tree = [[] for _ in range(N+1)]
    # 데이터에 가중치가 없으므로 그냥 뽑고 순환만 체크
    # 데이터를 순회하며 간선 연결
    # 양방향이기 때문에 편의상 앞의 데이터를 부모로 가정
    for parent, child in data_list:
        # 유니온-파인드
        state, union_list = union_find(parent, child, union_list)
        if not state:
            tree[parent].append(child)
    # 트리의 자식 수 합
    return sum([len(node) for node in tree])


# 프림
def prim(N, M, union_list, data_list):
    # 큐
    queue = deque([])
    # 트리, tree[parent] = childs
    tree = [[] for _ in range(N+1)]
    # 트리 구성
    for parent, child in data_list:
        tree[parent].append(child)
        tree[child].append(parent)
    # 자식의 수 리스트
    len_tree = [len(node) for node in tree]
    # 임의의 시작 노드, 간선이 가장 적어야함
    queue.append(len_tree.index(min(len_tree))+1)
    # 역시 데이터에 가중치가 없으므로 임의의 노드를 연결 후 순환 체크
    min_tree = [[] for _ in range(N+1)]
    # 데이터를 순회하며 간선 연결
    while True:
        # 큐가 비면 끝
        if not queue:
            # 트리의 자식 수 합
            return sum([len(node) for node in min_tree])
        # 현재 노드
        now_node = queue.popleft()
        for parent, child in data_list:
            # 현재 노드를 포함하고 있는 데이터라면
            if parent == now_node:
                state, union_list = union_find(parent, child, union_list)
                # 트리에 추가
                if not state:
                    min_tree[parent].append(child)
                    # 큐에 추가
                    queue.append(child)
            elif child == now_node:
                state, union_list = union_find(child, parent, union_list)
                # 트리에 추가
                if not state:
                    min_tree[child].append(parent)
                    # 큐에 추가
                    queue.append(parent)


T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    data_list = [list(map(int, input().split())) for __ in range(M)]
    solution(N, M, data_list)