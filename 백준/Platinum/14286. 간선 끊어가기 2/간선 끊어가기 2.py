import sys
from collections import deque

input = sys.stdin.readline


def solution(n, m, edges, s, t):
    # 최대 유량 최소 컷
    # 최소 컷은 최대유량과 같음
    # 양방향 간선 -> 노드를 두개로 분할
    # i 노드 -> i / i+n 노드로 분할
    # s 는 소스 / t+n 은 싱크
    s = s-1
    t = t-1

    # 그래프
    graph = [[] for _ in range(2*n)]
    # 분할 노드끼리 간선 연결
    for i in range(n):
        graph[i].append(i+n)
        graph[i+n].append(i)

    for a, b, c in edges:
        # 나가는 간선 연결
        graph[a-1].append(b-1)
        # 들어오는 간선 연결
        graph[b-1+n].append(a-1+n)
    
    # 흐를 수 있는 유량
    flowable = [[0 for _ in range(2*n)] for __ in range(2*n)]
    # 분할 노드끼리 유량
    for i in range(n):
        flowable[i][i+n] = float('inf')
        flowable[i+n][i] = float('inf')

    for a, b, c in edges:
        # 나가는 간선 유량
        flowable[a-1][b-1] += c
        # 들어오는 간선 유량
        flowable[b-1+n][a-1+n] += c
    
    # 최대 유량
    max_flow = 0
    # 싱크에 도달하지 못할 때 까지
    while True:
        # BFS 로 탐색
        # 데크
        dq = deque([s])
        # 방문 목록
        visited = [-1 for _ in range(2*n)]
        visited[s] = s
        # 순회
        while dq:
            # 데크에 마지막 지점이 들어왔으면
            if t+n in dq:
                break
            # 현재 노드
            now_node = dq.popleft()
            # 경로 순회
            for next_node in graph[now_node]:
                # 방문하지 않았고 이동할 수 있는 유체가 남아있으면
                if visited[next_node] == -1 and flowable[now_node][next_node] > 0:
                    # 큐에 삽입
                    dq.append(next_node)
                    # 방문 체크
                    visited[next_node] = now_node
        
        # 싱크에 도달하지 못했으면
        if not dq:
            break

        # 싱크에 도달했으면
        # 경로 추적
        route = deque([t+n])
        while route[0] != s:
            route.appendleft(visited[route[0]])

        # 이동시킬 유체량
        move_fluid = min([flowable[route[i]][route[i+1]] for i in range(len(route)-1)])
        # 최대 유량에 더해주기
        max_flow += move_fluid
        # 유체 이동
        for i in range(len(route)-1):
            flowable[route[i]][route[i+1]] -= move_fluid
            flowable[route[i+1]][route[i]] += move_fluid

    print(max_flow)


# 입력
n, m = map(int, input().strip().split())
edges = [list(map(int, input().strip().split())) for _ in range(m)]
s, t = map(int, input().strip().split())

solution(n, m, edges, s, t)