import sys
from collections import deque

input = sys.stdin.readline


def solution(N, M, gears):
    # 그래프
    graph = [[] for _ in range(N+1)]
    for x, y, k in gears:
        graph[x].append([y, k])
    
    # 위상 정렬 그래프 / [들어오는 노드의 수, 나가는 노드의 수]
    topol_list = [[0, 0] for _ in range(N+1)]
    topol_list[0] = [float('inf'), float('inf')]
    for parent, child, _ in gears:
        topol_list[parent][1] += 1
        topol_list[child][0] += 1

    # 필요한 부품의 수
    gears = [0 for _ in range(N+1)]
    gears[N] = 1
    # 큐
    q = deque([N])
    # 순회
    while q:
        # 현재 노드
        now_node = q.popleft()
        # 순회
        for next_node, mul in graph[now_node]:
            # 부품의 수 더해주기
            gears[next_node] += gears[now_node] * mul
            # 다음 노드의 들어오는 노드 빼주기
            topol_list[next_node][0] -= 1
            # 다음 노드의 들어오는 노드가 0 이면 큐에 넣어주기
            if not topol_list[next_node][0]:
                q.append(next_node)
    
    for gear in range(len(gears)):
        if not topol_list[gear][1]:
            print(f'{gear} {gears[gear]}')


# 입력
N = int(input().strip())
M = int(input().strip())
gears = [list(map(int, input().strip().split())) for _ in range(M)]

solution(N, M, gears)