from collections import deque
import sys

def solution(N, K, build_times, build_rules, W):
    # 인덱스 맞추기
    build_times = [0] + build_times
    # 위상정렬
    topolog_list = [[0, 0] for _ in range(N+1)]
    # 트리
    tree = [[] for _ in range(N+1)]
    # 트리 및 위상정렬 정리
    # 트리에는 다음으로 이동 가능한 노드가 들어감
    for start, end in build_rules:
        tree[start].append(end)
    # 위상정렬에는 들어가는 노드와 나오는 노드가 들어감
    for i, node in enumerate(tree):
        for j, num in enumerate(node):
            topolog_list[num][0] += 1
            topolog_list[i][1] += 1
    # 최대 시간
    max_times = [0 for _ in range(N+1)]
    # 들어가는 노드가 없는 노드를 큐에 넣음
    # 최대 시간도 최신화
    queue = deque([])
    for idx, (in_node, out_node) in enumerate(topolog_list):
        if not in_node and idx:
            queue.append(idx)
            max_times[idx] = build_times[idx]

    while True:
        # 큐가 비면 끝
        if not queue:
            return max_times[W]
        # 현재 노드
        now_node = queue.popleft()
        # 이동 가능한 노드중 들어가는 노드가 하나인 노드로 이동
        for node in tree[now_node]:
            # 들어가는 노드 하나씩 지우기
            topolog_list[node][0] -= 1
            # 최대시간과 비교해서 업데이트
            if max_times[node] < max_times[now_node] + build_times[node]:
                max_times[node] = max_times[now_node] + build_times[node]
            # 들어가는 노드가 없으면
            if not topolog_list[node][0]:
                # 다음 노드가 목적 노드가 아니면 큐에 추가
                if node != W:
                    queue.append(node)


T = int(input())
for _ in range(T):
    N, K = map(int, sys.stdin.readline().split())
    build_times = list(map(int, sys.stdin.readline().split()))
    build_rules = [list(map(int, sys.stdin.readline().split())) for _ in range(K)]
    W = int(sys.stdin.readline())
    print(solution(N, K, build_times, build_rules, W))