import sys
from collections import deque

input = sys.stdin.readline


def solution(N, works):
    # 위상정렬 그래프 / [[들어오는 노드들], 소요 시간, [나가는 노드들]]
    topol_graph = [[[], 0, []] for _ in range(N+1)]
    for w in range(len(works)):
        # 소요 시간
        topol_graph[w+1][1] = works[w][0]
        # 입출력 노드
        for i in range(works[w][1]):
            topol_graph[w+1][0].append(works[w][2+i])
            topol_graph[works[w][2+i]][2].append(w+1)
    
    # 작업 완료 여부
    finished = [0 for _ in range(N+1)]
    # 소요 시간 리스트
    times = [0 for _ in range(N+1)]
    # 큐
    q = deque()
    # 순회
    while True:
        # 선행 작업이 없는 노드들 삽입
        for node in range(1, len(topol_graph)):
            if not finished[node] and all([finished[i] for i in topol_graph[node][0]]):
                q.append([node, max(times[node], topol_graph[node][1])])
                # 작업을 완료한 시간 넣기
                times[node] = max(times[node], topol_graph[node][1])
                # 작업 완료
                finished[node] = 1
                break
        
        # 큐가 비었으면 끝
        if not q:
            break

        # 순회
        while q:
            # 현재 노드 / 현재 시간
            now_node, now_time = q.popleft()
            # 순회
            for next_node in topol_graph[now_node][2]:
                # 작업 완료 시간
                next_time = now_time + topol_graph[next_node][1] 
                # 작업을 완료하는 시간 넣기
                times[next_node] = max(times[next_node], next_time)

    print(max(times))


# 입력
N = int(input().strip())
works = [list(map(int, input().strip().split())) for _ in range(N)]

solution(N, works)