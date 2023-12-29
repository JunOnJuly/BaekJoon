import sys
from collections import deque
from math import log2


def solution(N, M, edge_list, data_list):
    # LCA 와 희소배열 이용
    # 트리의 최대 깊이
    max_depth = int(log2(N))+1
    # 트리 / tree[i] = [i 의 자식들]
    tree = [[] for _ in range(N+1)]
    for node_1, node_2 in edge_list:
        tree[node_1].append(node_2)
        tree[node_2].append(node_1)
    # 노드 깊이 기록 및 트리 정리
    depth_list, tree = set_node_depth(tree, N)
    # 희소 배열 / sparse_table[i][j] = j 노드의 2^(i) 위의 조상
    sparse_table = [tree[:] for _ in range(max_depth)]
    for i in range(1, max_depth):
        for j in range(1, N+1):
            # 조상 노드의 값이 -1 이면 기록하지 않음
            if sparse_table[i-1][j] > 0:
                sparse_table[i][j] = sparse_table[i-1][sparse_table[i-1][j]]
            else:
                sparse_table[i][j] = -1
    # 데이터 순회
    for node_1, node_2 in data_list:
        # 노드 깊이 맞추기
        node_1, node_2, depth = equalize_depth(node_1, node_2, depth_list, sparse_table)
        # 두 노드가 같으면 출력
        if node_1 == node_2:
            print(node_1)
            continue
        # 두 노드를 2^n 만큼 거슬러 올라갔을 때 두 노드가 같지 않을 때까지 반복
        for exp in range(max_depth-1, -1, -1):
            if sparse_table[exp][node_1] != sparse_table[exp][node_2]:
                # node_1 거슬러 올라가기
                node_1 = sparse_table[exp][node_1]
                # node_2 거슬러 올라가기
                node_2 = sparse_table[exp][node_2]
        # 끝까지 거슬러 올라갔을 때 부모가 공통 조상
        print(sparse_table[0][node_1])


# 노드 깊이 기록 및 트리 정리 함수
def set_node_depth(tree, N):
    # 정리된 트리 / fixed_tree[i] = i 의 부모 노드
    fixed_tree = [-1 for _ in range(N+1)]
    # BFS 사용을 위한 큐 / [노드, 깊이]
    queue = deque([[1, 0]])
    # 깊이 목록
    depth_list = [-1 for _ in range(N+1)]
    # 트리 순회
    while True:
        # 큐가 비면 리턴
        if not queue:
            return depth_list, fixed_tree
        # 현재 노드
        now_node, depth = queue.popleft()
        # 현재 깊이 기록
        depth_list[now_node] = depth
        # 연결되어 있는 노드 큐에 삽입
        for node in tree[now_node]:
            # 깊이가 기록되어 있지 않을 때만
            if depth_list[node] == -1:
               queue.append([node, depth+1])
               # 트리 정리
               fixed_tree[node] = now_node


# 노드 깊이 맞추기
def equalize_depth(node_1, node_2, depth_list, sparse_table):
    # 각 노드의 깊이
    depth_1 = depth_list[node_1]
    depth_2 = depth_list[node_2]
    # 맞춰질 깊이
    depth = min(depth_1, depth_2)
    # 1 이 깊으면
    if depth_1 > depth_2:
        # 깊이의 차이
        sub_depth = depth_1 - depth_2
        # 차이를 이진법으로 표현
        bin_sub_depth = list(reversed(bin(sub_depth)[2:]))
        # 1을 두 깊이의 차이만큼 내림
        for num_idx in range(len(bin_sub_depth)):
            # num 이 1이면
            if int(bin_sub_depth[num_idx]):
                node_1 = sparse_table[num_idx][node_1]
    # 2 가 깊으면
    elif depth_1 < depth_2:
        # 깊이의 차이
        sub_depth = depth_2 - depth_1
        # 차이를 이진법으로 표현
        bin_sub_depth = list(reversed(bin(sub_depth)[2:]))
        # 1을 두 깊이의 차이만큼 내림
        for num_idx in range(len(bin_sub_depth)):
            # num 이 1이면
            if int(bin_sub_depth[num_idx]):
                node_2 = sparse_table[num_idx][node_2]
    return node_1, node_2, depth
        

N = int(sys.stdin.readline())
edge_list = [list(map(int, sys.stdin.readline().split())) for _ in range(N-1)]
M = int(sys.stdin.readline())
data_list = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(M)]
solution(N, M, edge_list, data_list)