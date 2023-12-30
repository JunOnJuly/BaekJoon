import sys
from math import log2
from collections import deque
from copy import deepcopy
input = sys.stdin.readline


def solution(N, K, edge_list, data_list):
    # LCA 문제 변형
    # 임시 트리, tree[i] = [[i와 연결된 노드, 길이], ...]
    # 모든 노드가 연결되어 있으므로 임의의 방향으로 간선을 정렬해도 상관 없음
    tree = [[] for _ in range(N+1)]
    tree[0] = [-1]
    for node_1, node_2, dist in edge_list:
        tree[node_1].append([node_2, dist])
        tree[node_2].append([node_1, dist])
    # 트리 정렬 및 노드 깊이 찾기
    tree, depth_list = find_depth(tree, N)
    # 희소 배열 만들기
    sparse_table = set_sparse_table(tree, N)
    # 데이터 순회
    for node_1, node_2 in data_list:
        # 깊이 맞추기
        node_1, node_2, depth, min_dist, max_dist = equailze_depth(node_1, node_2, depth_list, tree, sparse_table)
        # node_1 과 node_2 가 같으면 프린트
        if node_1 == node_2:
            print(f'{min_dist} {max_dist}')
            continue
        # 이동할 수 있는 2^n 씩 이동하며 최소, 최댓값 갱신
        for step in range(int(log2(N)), -1, -1):
            # 이동한 노드가 같은 노드면 패스
            if sparse_table[step][node_1][0] == sparse_table[step][node_2][0]:
                continue
            # 아니면 이동
            else:
                node_1, min_1, max_1 = sparse_table[step][node_1]
                node_2, min_2, max_2 = sparse_table[step][node_2]
            # 최소 최대 길이 갱신
            min_dist = min(min_dist, min_1, min_2)
            max_dist = max(max_dist, max_1, max_2)
        # 끝까지 왔으면 부모가 최소 공통 조상이므로 부모까지 최소 최대값 갱신
        lca, min_lca_1, max_lca_1 = sparse_table[0][node_1]
        lca, min_lca_2, max_lca_2 = sparse_table[0][node_2]
        min_dist = min(min_dist, min_lca_1, min_lca_2)
        max_dist = max(max_dist, max_lca_1, max_lca_2)
        print(f'{min_dist} {max_dist}')


# 트리 정렬 및 노드 깊이 찾기 함수
def find_depth(tree, N):
    # 노드 깊이 리스트
    depth_list = [-1 for _ in range(N+1)]
    # 큐, queue[i] = [노드 인덱스, 깊이]
    # 어차피 N 개의 도시와 N-1 개의 도로면 순환없음
    # 아무 노드나 루트로, 1번
    queue = deque([[1, 0]])
    # 정렬된 트리, tree[i] = [i 의 부모, 간선의 길이, 간선의 길이], 희소배열 세팅
    sorted_tree = [[None, None, None] for _ in range(N+1)]
    sorted_tree[1] = [1, 1000000, 0]
    # BFS
    while queue:
        # 현재 노드, 깊이
        now_node, depth = queue.popleft()
        # 깊이 리스트 최신화
        depth_list[now_node] = depth
        # 연결된 노드 탐색
        for node, dist in tree[now_node]:
            # 탐색하지 않은 노드만
            if depth_list[node] < 0:
                # 큐에 추가
                queue.append([node, depth+1])
                # 부모 노드 추가
                sorted_tree[node] = [now_node, dist, dist]
    return sorted_tree, depth_list


# 희소 배열 만들기 함수
def set_sparse_table(tree, N):
    # 희소 배열 최대 행 길이
    max_row = int(log2(N))+1
    # 희소 배열, sparse_table[i][j] = [j의 2^i 번째 조상, 그때까지의 최소, 최대 길이]
    sparse_table = [deepcopy(tree) for _ in range(max_row)]
    # 배열 최신화
    for i in range(1, max_row):
        for j in range(1, N+1):
            sparse_table[i][j] = \
                [sparse_table[i-1][sparse_table[i-1][j][0]][0],\
                 min(sparse_table[i-1][j][1], sparse_table[i-1][sparse_table[i-1][j][0]][1]),\
                 max(sparse_table[i-1][j][2], sparse_table[i-1][sparse_table[i-1][j][0]][2])]
    return sparse_table


# 노드 깊이 맞추기 함수
def equailze_depth(node_1, node_2, depth_list, tree, sparse_table):
    # 각 노드의 깊이
    depth_1 = depth_list[node_1]
    depth_2 = depth_list[node_2]
    # 맞춰질 높이
    depth = min(depth_1, depth_2)
    # 최소 최대 길이 선언
    min_dist = 1000000
    max_dist = 0
    # 희소배열 사용 
    while depth_1 != depth_2:
        # 1 의 깊이가 깊으면 node 1 끌어올리기
        if depth_1 > depth_2:
            # 깊이 차이
            sub_depth = depth_1-depth_2
            # 깊이 차이 2진수
            bin_sub_depth = bin(sub_depth)[2:]
            # 순회
            for num_idx, num in enumerate(reversed(bin_sub_depth)):
                # 1 이면 노드 이동
                if int(num):
                    min_dist = min(min_dist, sparse_table[num_idx][node_1][1])
                    max_dist = max(max_dist, sparse_table[num_idx][node_1][2])
                    node_1 = sparse_table[num_idx][node_1][0]
                    depth_1 = depth_list[node_1]
        # 2 의 깊이가 깊으면 node 2 끌어올리기
        elif depth_1 < depth_2:
            # 깊이 차이
            sub_depth = depth_2-depth_1
            # 깊이 차이 2진수
            bin_sub_depth = bin(sub_depth)[2:]
            # 순회
            for num_idx, num in enumerate(reversed(bin_sub_depth)):
                # 1 이면 노드 이동
                if int(num):
                    min_dist = min(min_dist, sparse_table[num_idx][node_2][1])
                    max_dist = max(max_dist, sparse_table[num_idx][node_2][2])
                    node_2 = sparse_table[num_idx][node_2][0]
                    depth_2 = depth_list[node_2]
    return node_1, node_2, depth, min_dist, max_dist


N = int(input())
edge_list = [list(map(int, input().split())) for _ in range(N-1)]
K = int(input())
data_list = [list(map(int, input().strip().split())) for _ in range(K)]
solution(N, K, edge_list, data_list)