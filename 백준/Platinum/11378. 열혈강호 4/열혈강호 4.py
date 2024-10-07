import sys
from collections import deque, defaultdict

input = sys.stdin.readline


def solution(N, M, K, hope_list):
    # 흐를수 있는 유체의 양
    flowable = defaultdict(lambda : defaultdict(int))
    ### 0 : 소스 / 1 ~ N : 직원 / N+1 ~ N+M : 일 / N+M+1 : 추가 인력 / N+M+2 : 싱크
    ## 소스 ~ 직원 ~ 일 ~ 싱크
    # 모든 직원은 기본적으로 일을 한 개씩은 할 수 있음
    for i in range(1, N+1):
        flowable[0][i] = 1
    # 직원은 할 수 있는일을 고름
    for i in range(len(hope_list)):
        for j in hope_list[i]:
            flowable[i+1][N+1+j] = 1
    # 모든 처리한 일은 싱크로
    for i in range(M):
        flowable[N+1+i][N+M+2] = 1
    ## 소스 ~ 추가인력 ~ 직원 ~ 일 ~ 싱크
    # 추가 인력을 모두 추가인력 노드에 넣어줌
    flowable[0][N+M+1] = K
    # 운이 안좋으면 한명이 1+K 개의 일을 할지도..
    for i in range(1, N+1):
        flowable[N+M+1][i] = K
    
    # 노드에 있는 유체의 양
    fluid = [N+M+K] + [0 for _ in range(N+M+2)]

    # 네트워크 플로우
    # 싱크에 도달할 수 없을 때 까지
    while True:
        # 데크
        dq = deque([0])
        # 방문 목록
        visited = [-1 for _ in range(N+M+3)]
        # BFS
        while dq:
            # 싱크에 도달했으면
            if dq[-1] == N+M+2:
                break
            # 현재 노드
            now_node = dq.popleft()
            # 이동할 수 있는 노드 탐색
            for next_node, flow in flowable[now_node].items():
                # 방문하지 않았고 유체가 흐를 수 있으면
                if visited[next_node] < 0 and flow:
                    # 데크에 삽입
                    dq.append(next_node)
                    # 방문 기록
                    visited[next_node] = now_node
        
        # 싱크에 도달하지 못했으면
        if not dq:
            # 끝
            break

        # 경로
        route = deque([N+M+2])
        # 경로에서 흐를 수 있는 유체량의 최댓값
        max_flow = float('inf')
        # 순회
        while True:
            # 현재 노드
            now_node = route[0]
            # 직전 노드
            before_node = visited[now_node]
            # 경로에 삽입
            route.appendleft(before_node)
            # 흐를 수 있는 유체량의 최댓값 갱신
            max_flow = min(max_flow, flowable[before_node][now_node])
            # 직전 노드가 소스면 끝
            if before_node == 0:
                break

        # 경로를 따라 흐를 수 있는 최댓값 흘려주기
        for i in range(len(route)-1):
            # 경로에서 빼주기
            flowable[route[i]][route[i+1]] -= max_flow
            # 반대방향으로는 더해주기
            flowable[route[i+1]][route[i]] += max_flow
            # 출발 노드 유체 빼주기
            fluid[route[i]] -= max_flow
            # 도착 노드 유체 더해주기
            fluid[route[i+1]] += max_flow

    # 싱크의 유체 반환
    print(fluid[-1])


# 입력
N, M, K = map(int, input().strip().split())
connectable = [list(map(lambda x: int(x)-1, input().strip().split()))[1:] for _ in range(N)]
solution(N, M, K, connectable)