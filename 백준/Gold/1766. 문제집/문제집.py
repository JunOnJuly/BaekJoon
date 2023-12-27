import sys


def solution(N, M, data_list):
    # 위상정렬 알고리즘
    # 트리, tree[i] = [[i 의 자식들], i 노드로 들어오는 간선의 수]
    tree = [[[], 0] for _ in range(N+1)]
    tree[0][1] = -1
    # 데이터 순회하며 트리 최신화
    for parent, child in data_list:
        # 자식 추가
        tree[parent][0].append(child)
        # 자식으로 들어가는 간선 추가
        tree[child][1] += 1
    # 수가 낮은 노드먼저 순회할 수 있게 트리 내부의 자식들 정렬
    for node in tree:
        node[0] = sorted(node[0])
    # 정렬된 리스트
    sorted_list = []
    # 진입차수(들어오는 간선의 수)가 0 인 가장 작은 노드 큐에 추가
    for node_idx in range(len(tree)):
        if not tree[node_idx][1]:
            sorted_list.append(node_idx)
            # 해당 노드 진입차수 -1
            tree[node_idx][1] -= 1
            # 해당 노드와 연결된 노드 진입차수 -1
            for linked_node_idx in tree[node_idx][0]:
                tree[linked_node_idx][1] -= 1
            break
    # 순회  
    while len(sorted_list) != N:
        # 진입차수(들어오는 간선의 수)가 0 인 가장 작은 노드 큐에 추가
        for node_idx in range(len(tree)):
            if not tree[node_idx][1]:
                sorted_list.append(node_idx)
                # 해당 노드 진입차수 -1
                tree[node_idx][1] -= 1
                # 해당 노드와 연결된 노드 진입차수 -1
                for linked_node_idx in tree[node_idx][0]:
                    tree[linked_node_idx][1] -= 1
                break
    print(*sorted_list)


N, M = map(int, sys.stdin.readline().split())
data_list = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(M)]
solution(N, M, data_list)