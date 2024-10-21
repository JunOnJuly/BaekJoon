import sys
from collections import deque

input = sys.stdin.readline


# 이분매칭
def bimatch(idx, connectable, connected, visited):
    # 방문했다면 패스
    if visited[idx]:
        return False
    
    # 방문 체크
    visited[idx] = True
    # 순회
    for node in connectable[idx]:
        # 선택할 수 있거나 옮길 수 있으면
        if connected[node] < 0 or bimatch(connected[node], connectable, connected, visited):
            # 선택
            connected[node] = idx
            
            return True
    
    return False


def solution(N, M, edges):
    # 매칭 가능 목록 A -> B
    connectable = [[] for _ in range(N+1)]
    for i in range(len(edges)):
        for j in range(len(edges[i])):
            connectable[i+1].append(edges[i][j])
    
    # 최소 버텍스 커버 탐색을 위한 그래프
    graph = [[] for _ in range(N+M+1)]
    for i in range(len(edges)):
        for j in range(len(edges[i])):
            graph[i+1].append(N+edges[i][j])
            graph[N+edges[i][j]].append(i+1)

    # 매칭된 목록
    connected = [-1 for _ in range(M+1)]
    
    # 순회
    for idx in range(1, N+1):
        # 방문 목록
        visited = [False for _ in range(N+1)]
        # 이분매칭
        bimatch(idx, connectable, connected, visited)

    # 매칭되지 않은 좌측 / 매칭된 우측 노드군
    L = set(range(1, N+1)) - set(connected)
    R = set([c+N for c in range(len(connected)) if connected[c] >= 0])
    # 좌측 노드군에서 도달할 수 있는 alternating path
    X = list(L)
    # 데크
    dq = deque([[l, True] for l in L])
    # 방문 목록
    visited = [False for _ in range(len(graph))]
    for node in L:
        visited[node] = True
    # BFS 로 순회
    while dq:
        # 현재 노드 / 차수
        now_node, state = dq.popleft()

        # 다음 탐색 가능 노드 순회
        for node in graph[now_node]:
            # 방문하지 않았고 매칭 여부가 교차된 엣지면
            if not visited[node]:
                # 전에 매칭된 엣지고 다음 엣지는 매칭 안된 엣지면
                # 전에 매칭안된 엣지고 다음 엣지는 매칭된 엣지면
                if (state and connected[node-N] != now_node) or \
                    (not state and connected[now_node-N] == node):
                    # 데크에 추가
                    dq.append([node, not state])
                    # 방문 체크
                    visited[node] = True
                    # 노드군 추가
                    X.append(node)

    X = sorted(list(set(X)))

    # 출력
    print(sum([1 for c in connected if c >= 0]))
    print(sum([1 for x in set(range(1, N+1))-set(X) if x <= N]), end=' ')
    print(*[x for x in set(range(1, N+1))-set(X) if x <= N])
    print(sum([1 for x in set(X)&R if x > N]), end=' ')
    print(*[x-N for x in set(X)&R if x > N])


# 입력
N, M = map(int, input().strip().split())
edges = [list(map(int, input().strip().split()[1:])) for _ in range(N)]

solution(N, M, edges)