import sys
from collections import deque, defaultdict

input = sys.stdin.readline


def solution(N, M, K, hope_list):
    # 흐를 수 있는 유량
    # flowable[i] = [[i 와 연결된 노드, 흐를 수 있는 유량], ...]
    # 0 : 소스 / 1 ~ N : 직원 / N+1 ~ N+M : 일 / N+M+1 : 추가 인력 노드 / N+M+2 : 싱크
    flowable = defaultdict(lambda : defaultdict(int))
    
    ## 소스 -> 직원 -> 일 -> 싱크
    # 소스에서 직원에게 1 씩 일을 할당 가능
    for i in range(1, N+1):
        flowable[0][i] = 1
    # 직원은 하고싶은 일을 선택 가능
    for i in range(len(hope_list)):
        for j in range(len(hope_list[i])):
            flowable[i+1][hope_list[i][j]+N+1] = 1
    # 일은 모두 싱크로 흘러감
    for i in range(N+1, N+M+1):
        flowable[i][N+M+2] = 1
    
    ## 소스 -> 추가 인력 -> 직원
    # 소스에서 추가 인력노드로 추가인력 모두 할당 가능
    flowable[0][N+M+1] = K
    # 추가 인력 노드는 모든 직원에게 인력 충원 가능
    for i in range(1, N+1):
        flowable[N+M+1][i] = 1

    # 현재 노드에 있는 유량
    fluid = [N+K] + [0 for _ in range(N+M+2)]

    # 네트워크 플로우
    # 싱크에 도달할 수 없을 때 까지
    while True:
        # 데크
        dq = deque([0])
        # 방문목록
        # visited[i] = 직전노드
        visited = [-1 for _ in range(N+M+3)]
        visited[0] = 0
        # BFS
        while dq:
            # 싱크에 도달했으면
            if dq[-1] == N+M+2:
                # 종료
                break
            # 현재 노드
            now_node = dq.popleft()
            # 이동 가능한 노드 순회
            for node, flow in flowable[now_node].items():
                # 방문하지 않았고 흐를 수 있는 유량이 존재하면
                if visited[node] < 0 and flow:
                    # 큐에 삽입
                    dq.append(node)
                    # 방문 체크
                    visited[node] = now_node
                    
        # 데크가 비어있다면 끝
        if not dq:
            break

        # 방문목록을 역순회해 경로 추적 및 흐를 수 있는 유체량 추적
        # 경로
        route = deque([N+M+2])
        # 흐를 수 있는 유체의 최대량
        max_flow = float('inf')
        # 경로 추적
        now_node = N+M+2
        while now_node != 0:
            # 직전 노드
            before_node = visited[now_node]
            # 경로에 추가
            route.appendleft(before_node)
            # 유체의 최대량 업데이트
            max_flow = min(max_flow, flowable[before_node][now_node])
            # 노드 최신화
            now_node = before_node

        # 경로를 따라 유체 흘려주기
        for i in range(len(route)-1):
            flowable[route[i]][route[i+1]] -= max_flow
            # 반대로도 흘려주기
            flowable[route[i+1]][route[i]] += max_flow
            # 유체량 업데이트
            fluid[route[i]] -= max_flow
            fluid[route[i+1]] += max_flow

    # 싱크에 있는 유량 리턴
    print(fluid[-1])


# 입력
N, M, K = map(int, input().strip().split())
hope_list = [list(map(lambda x: int(x)-1, input().strip().split()))[1:] for n in range(N)]
solution(N, M, K, hope_list)