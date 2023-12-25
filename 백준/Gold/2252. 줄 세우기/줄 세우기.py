import sys
from collections import deque


def solution(N, M, data_list):
    # 큐
    queue = deque([])
    # 위상정렬을 위한 간선정보를 포함한 트리 [[자식 노드들], 들어오는 간선] 
    tree = [[[], 0] for _ in range(N+1)]
    tree[0][1] = -1
    # 간선 정보 입력
    for parent, child in data_list:
        # 자식 정보 입력
        tree[parent][0].append(child)
        # 자식의 들어오는 간선 + 1
        tree[child][1] += 1
    # 트리에서 들어오는 간선이 0 인 노드 모두 큐에 추가
    for node_idx in range(len(tree)):
        if not tree[node_idx][1]:
            queue.append(node_idx)
    # 줄세우기 리스트
    line = []
    # 순회
    while True:
        # 큐가 비면 끝
        if not queue:
            print(*line)
            return
        # 현재 노드
        now_node = queue.popleft()
        # 현재 노드 줄세우기 리스트에 추가
        line.append(now_node)
        # 현재 노드의 간선 -1 으로 중복 방지
        tree[now_node][1] -= 1
        # 현재 노드에 연결되어 있는 노드 간선 제거
        for node in tree[now_node][0]:
            tree[node][1] -= 1
        # 현재 노드에 연결되어 있는 노드 중 들어오는 간선이 0 이면 큐에 삽입
        for node in tree[now_node][0]:
            if not tree[node][1]:
                queue.append(node)


N, M = map(int, sys.stdin.readline().split())
data_list = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
solution(N, M, data_list)