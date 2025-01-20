import sys
from dataclasses import dataclass
from collections import defaultdict

input = sys.stdin.readline


# 노드
@dataclass
class Node:
    level: int
    left: int
    right: int


# 중위 순회
def inorder(nodes, informs, node, level, idx):
    # 레벨 기록
    informs[node][0] = level
    # 왼쪽 노드가 존재하면
    if nodes[node].left > 0:
        # 재귀
        idx = inorder(nodes, informs, nodes[node].left, level+1, idx)
    
    # 위치 기록
    informs[node][1] = idx
    # 인덱스 + 1
    idx += 1

    # 오른쪽 노드가 존재하면
    if nodes[node].right > 0:
        # 재귀
        idx = inorder(nodes, informs, nodes[node].right, level+1, idx)
    
    return idx


def solution(N, nodes):
    # 노드 정리
    nodes = defaultdict(Node, {i:Node(0, l, r) for i, l, r in nodes})
    # 루트노드 찾기 == 자식으로 지정되지 않은 노드
    nodes_counts = [0 for _ in range(N+1)]
    for node in nodes.values():
        if node.left > 0:
            nodes_counts[node.left] += 1
        if node.right > 0:
            nodes_counts[node.right] += 1
    
    root_node = nodes_counts[1:].index(0) + 1
    # 레벨 / 위치 기록
    informs = [[0, 0] for _ in range(N+1)]
    # 중위 순회
    inorder(nodes, informs, root_node, 1, 1)
    # 기록 정리
    informs_dict = defaultdict(list)
    for level, idx in sorted(informs[1:], key=lambda x: (x[0], x[1])):
        informs_dict[level].append(idx)

    # 최댓값
    max_width = 0
    # 최댓값에 해당하는 레벨
    max_level = 0
    # 순회
    for level, idxs in informs_dict.items():
        # 레벨당 너비
        width = max(idxs) - min(idxs) + 1
        # 최댓값 갱신
        if width > max_width:
            max_width = width
            max_level = level
    
    print(f'{max_level} {max_width}')


# 입력
N = int(input().strip())
nodes = [list(map(int, input().strip().split())) for _ in range(N)]

solution(N, nodes)