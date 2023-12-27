import sys


def solution(N, data_list, target_node):
    # LCA(최소 공통 조상) 알고리즘
    # 트리, tree[i] = [부모 노드, [자식 노드들]]
    tree = [[None, []] for _ in range(N+1)]
    for parent, child in data_list:
        # 자식 추가
        tree[parent][1].append(child)
        # 부모 추가
        tree[child][0] = parent
    # 깊이 리스트
    depth_list = [0 for _ in range(N+1)]
    # 조상 리스트, an~[i] = [조상1, 조상2, ...]
    ancestor_list = [[] for _ in range(N+1)]
    # 스택
    stack = []
    # 부모가 없는 노드 스택에 추가(루트 노드)
    for node_idx in range(1, len(tree)):
        if not tree[node_idx][0]:
            stack.append([node_idx, 0])
            break
    # 최하단 노드 기록
    deepest_node_list = [0 for _ in range(N+1)]
    # 깊이 리스트 채우기, DFS
    while stack:
        # 현재 노드
        now_node, depth = stack[-1]

        # # # 조상 리스트에 추가
        # # ancestor_list[now_node] = [node[0] for node in stack]

        # 깊이 리스트에 추가
        depth_list[now_node] = depth
        # 현재 노드의 자식 순회
        # 자식 노드가 있으면
        if tree[now_node][1]:
            for node_idx in range(len(tree[now_node][1])):
                # 방문한 적 없으면 스택에 추가
                if not depth_list[tree[now_node][1][node_idx]]:
                    stack.append([tree[now_node][1][node_idx], depth+1])
                    break
                # 모든 노드가 방문한 상태면 팝
                elif node_idx == len(tree[now_node][1])-1:
                    stack.pop()
        # 없으면
        else:
            # 최하단 노드 기록
            for node in stack:
                deepest_node_list[node[0]] = now_node
            # 조상 리스트 추가
            ancestor_list[now_node] = [node[0] for node in stack]
            stack.pop()
    # 깊이 맞추기
    node_1, node_2, depth = set_depth(target_node[0], target_node[1], depth_list, ancestor_list, deepest_node_list)
    # 이분탐색으로 같은 노드 검색
    start = 0
    end = depth
    # 마지막으로 일치한 노드
    LCA_node = 0
    while start <= end:
        # 중간
        half = (start+end)//2
        # 중간 깊이에서 같은 노드면 하위 노드 검색
        if ancestor_list[deepest_node_list[node_1]][half] == ancestor_list[deepest_node_list[node_2]][half]:
            # 일치노드 최신화
            LCA_node = ancestor_list[deepest_node_list[node_1]][half]
            # 하위 노드로 이동
            start = half+1
        # 다른 노드면 상위 노드 검색
        else:
            end = half-1
    print(LCA_node)


# 깊이 맞추기
def set_depth(node_1, node_2, depth_list, ancestor_list, deepest_node_list):
    # 둘의 깊이 차이
    sub_depth = depth_list[node_1] - depth_list[node_2]
    # 맞춰진 깊이
    depth = min(depth_list[node_1], depth_list[node_2])
    # node_1 이 크면
    if sub_depth > 0:
        node_1 = ancestor_list[deepest_node_list[node_1]][depth_list[node_1]-sub_depth]
    elif sub_depth < 0:
        node_2 = ancestor_list[deepest_node_list[node_2]][depth_list[node_2]+sub_depth]
    return node_1, node_2, depth
       

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    data_list = [list(map(int, sys.stdin.readline().split())) for __ in range(N-1)]
    target_node = list(map(int, sys.stdin.readline().strip().split()))
    solution(N, data_list, target_node)