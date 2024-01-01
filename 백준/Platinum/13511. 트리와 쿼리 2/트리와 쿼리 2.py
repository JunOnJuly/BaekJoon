from collections import deque
from math import log2
import sys
input = sys.stdin.readline


def solution(N, M, edge_list, query_list):
    # 최소 공통 조상 구해서 다시 거슬러 올라가자 / 과정 모두 저장하면 메모리 초과
    # 임시 트리 기록 / tree[i] = [[i 노드의 자식, 비용] ... ]
    tree = [[] for _ in range(N+1)]
    for node_1, node_2, cost in edge_list:
        tree[node_1].append([node_2, cost])
        tree[node_2].append([node_1, cost])
    # 트리 정렬 및 깊이 탐색
    tree, depth_list = sort_tree_and_set_depth(tree, N)
    # 희소배열 생성
    sparse_table = set_sparse_table(tree, N)
    # 쿼리 순회
    for query in query_list:
        # 쿼리 상태
        state = query[0]
        # 노드
        node_1 = query[1]
        node_2 = query[2]
        # 깊이 맞추기
        eq_node_1, eq_node_2, cost = equailze_depth(node_1, node_2, depth_list, sparse_table)
        # eq_node_1 이 eq_node_2 면 lca 는 eq_node_1 == eq_node_2
        if eq_node_1 == eq_node_2:
            lca = eq_node_1
        else:
            # 순회
            for n in range(int(log2(N)), -1, -1):
                # 큰 수부터 올라가보며 같은 노드면 패스
                if sparse_table[n][eq_node_1][0] != sparse_table[n][eq_node_2][0]:
                    # 코스트 추가
                    cost += sparse_table[n][eq_node_1][1]+sparse_table[n][eq_node_2][1]
                    # 노드 이동
                    eq_node_1 = sparse_table[n][eq_node_1][0]
                    eq_node_2 = sparse_table[n][eq_node_2][0]
            # 순회가 끝나면 하나 더 거슬러 올라가기
            # 코스트 추가
            cost += sparse_table[0][eq_node_1][1]+sparse_table[0][eq_node_2][1]
            # lca
            lca = sparse_table[0][eq_node_1][0]
        # state 가 1 이면
        if state == 1:
            print(cost)
            continue
        # 아니면
        else:
            # node와 lca 의 거리
            dist_node_1 = depth_list[node_1] - depth_list[lca] + 1
            dist_node_2 = depth_list[node_2] - depth_list[lca] + 1
            # 순회
            k = query[3]
            # dist_node_1 보다 k 가 크면
            if k > dist_node_1:
                # node_2 에서 거슬러 올라감
                # node_2 에서부터 k 의 위치
                dist_k = dist_node_1 + dist_node_2 - 1 - (k-1)
                # 2진법
                bin_dist_k = bin(dist_k-1)[2:]
                for idx, n in enumerate(reversed(bin_dist_k)):
                    if n == '1':
                        node_2 = sparse_table[idx][node_2][0]
                print(node_2)
                continue
            # dist_node_1 보다 k 가 작으면
            elif k < dist_node_1:
                # node_1 에서 거슬러 올라감
                # 2진법
                bin_dist_k = bin(k-1)[2:]
                for idx, n in enumerate(reversed(bin_dist_k)):
                    if n == '1':
                        node_1 = sparse_table[idx][node_1][0]
                print(node_1)
                continue
            # 같으면
            else:
                print(lca)
                continue
            
            
# 트리 정렬 및 깊이 탐색 함수
def sort_tree_and_set_depth(tree, N):
    # 큐 / 1을 루트로 임의로 지정
    queue = deque([[1, 0]])
    # 깊이 리스트
    depth_list = [0] + [-1 for _ in range(N)]
    # 정렬된 트리 / tree[i] = [i 의 부모, 비용]
    sorted_tree = [[] for _ in range(N+1)]
    sorted_tree[1] = [1, 0]
    # 트리 탐색
    while queue:
        # 현재 노드, 깊이
        now_node, depth = queue.popleft()
        # 현재 노드 깊이 기록
        depth_list[now_node] = depth
        # 현재 노드와 연결되어 있고 깊이가 지정되지 않은 노드 탐색
        for node, cost in tree[now_node]:
            if depth_list[node] < 0:
                # 큐에 추가
                queue.append([node, depth+1])
                # 트리에 추가
                sorted_tree[node] = [now_node, cost]
    return sorted_tree, depth_list


# 희소 배열 생성 함수
def set_sparse_table(tree, N):
    # 희소 배열 최대 행 개수
    max_row = int(log2(N))+1
    # 희소 배열 / sparse_table[i][j] = [j 노드의 2^i 번째 조상, 조상 노드까지의 비용]
    sparse_table = [[[]] + [[tree[i][0], tree[i][1]] for i in range(1, N+1)] for _ in range(max_row)]
    # 희소 배열 최신화
    for i in range(1, max_row):
        for j in range(2, N+1):
            sparse_table[i][j] = [
                # 조상
                sparse_table[i-1][sparse_table[i-1][j][0]][0],
                # 비용
                sparse_table[i-1][j][1]+sparse_table[i-1][sparse_table[i-1][j][0]][1],
            ]
    return sparse_table


# 깊이 맞추기 함수
def equailze_depth(node_1, node_2, depth_list, sparse_table):
    # 노드들의 깊이
    depth_1 = depth_list[node_1]
    depth_2 = depth_list[node_2]
    # 이동 비용
    move_cost = 0
    # 깊이 상태, 1, 2 중에 뭐가 깊은지
    depth_state = 0
    # 깊이 차이
    sub_depth = 0
    # depth_1 이 더 크면
    if depth_1 > depth_2:
        # 깊이 상태
        depth_state = 1
        # 깊이 차이
        sub_depth = depth_1 - depth_2
        # 깊이 차이 2진수
        bin_sub_depth = bin(sub_depth)[2:]
        # 순회하며 노드 이동
        for idx, n in enumerate(reversed(bin_sub_depth)):
            # n 이 1 이면
            if n == '1':
                # 이동 비용 합
                move_cost += sparse_table[idx][node_1][1]
                # 노드 이동
                node_1 = sparse_table[idx][node_1][0]
    # depth_2 가 더 크면
    elif depth_1 < depth_2:
        # 깊이 상태
        depth_state = 2
        # 깊이 차이
        sub_depth = depth_2 - depth_1
        # 깊이 차이 2진수
        bin_sub_depth = bin(sub_depth)[2:]
        # 순회하며 노드 이동
        for idx, n in enumerate(reversed(bin_sub_depth)):
            # n 이 1 이면
            if n == '1':
                # 이동 비용 합
                move_cost += sparse_table[idx][node_2][1]   
                # 노드 이동
                node_2 = sparse_table[idx][node_2][0]
    return node_1, node_2, move_cost


N = int(input())
edge_list = [list(map(int, input().split())) for _ in range(N-1)]
M = int(input())
query_list = [list(map(int,input().strip().split())) for _ in range(M)]
solution(N, M, edge_list, query_list)