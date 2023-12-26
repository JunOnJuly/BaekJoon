import sys
from collections import deque


def solution(n, m, before_line, changed_list):
    # 리스트에서 바뀐 순서만 뽑아 재배치 후 다시 삽입
    # 위상정렬
    # 큐
    queue = deque([])
    # 이전 리스트에서 각 번호들의 순서 리스트, idx_list[num] = idx
    idx_list = [0 for _ in range(n+1)]
    for idx in range(len(before_line)):
        idx_list[before_line[idx]] = idx
    # 바뀐 리스트를 순회하며 위상정렬 트리 완성
    # tree[i] = [[i 의 자식들], i 에 들어오는 노드 수]
    tree = [[[], 0] for _ in range(n+1)]
    tree[0][1] = -1
    for num1, num2 in changed_list:
        # 원래 앞이었으면 뒤, 뒤였으면 앞
        if idx_list[num1] > idx_list[num2]:
            # 자식 추가
            tree[num1][0].append(num2)
            # 들어오는 노드 추가
            tree[num2][1] += 1
        else:
            # 자식 추가
            tree[num2][0].append(num1)
            # 들어오는 노드 추가
            tree[num1][1] += 1
    # 이전 줄 정보 트리에 추가
    for parent_idx in range(len(before_line)-1):
        for child_idx in range(parent_idx+1, len(before_line)):
            # 이미 등록된 정보가 없다면
            if before_line[parent_idx] not in tree[before_line[child_idx]][0]:
                # 자식 추가
                tree[before_line[parent_idx]][0].append(before_line[child_idx])
                # 들어오는 노드 추가
                tree[before_line[child_idx]][1] += 1
    # 들어오는 노드가 0 이면
    for node_idx in range(len(tree)):
        if not tree[node_idx][1]:
            queue.append(node_idx)
    # 바뀐 줄
    changed_line = []
    # 순회, 큐가 비면 끝
    while queue:
        # 큐에 노드가 둘 이상 들어있으면 ? 출력
        if len(queue) > 1:  
            print('?')
            return
        # 현재 노드
        now_node = queue.popleft()
        # 현재 노드 들어오는 간선 -1 처리로 중복 제거
        tree[now_node][1] -= 1
        # 현재 노드 바뀐 줄에 삽입
        changed_line.append(now_node)
        # 현재 노드와 연결된 노드 간선 제거
        for node in tree[now_node][0]:
            tree[node][1] -= 1
            # 현재 노드와 연결된 노드 중 들어오는 노드가 0 인 노드 큐에 삽입
            if not tree[node][1]:
                queue.append(node)
    # 순회가 끝났는데 바뀐 줄에 총 노드만큼 노드가 없으면 어디선가 순환이 생긴 것
    if len(changed_line) != n:
        print('IMPOSSIBLE')
    else:
        print(*changed_line)


T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    before_line = list(map(int, sys.stdin.readline().split()))
    m = int(sys.stdin.readline())
    changed_list = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(m)]
    solution(n, m, before_line, changed_list)