import sys
from collections import deque

input = sys.stdin.readline


def solution(N, P, edges):
    # 네트워크 플로우
    # 1, 2 가 싱크, 소스

    # 그래프
    graph = [[] for _ in range(N)]
    # 흐를 수 있는 유량
    flowable  = [[0 for _ in range(N)] for __ in range(N)]
    for n1, n2 in edges:
        # 그래프
        graph[n1].append(n2)
        graph[n2].append(n1)
        # 유량
        flowable[n1][n2] = 1
    
    # 현재 유량
    liquid = [0 for _ in range(N)]
    # 경로의 수
    cnt = 0
    # 순회
    while True:
        # 데크
        dq = deque([0])
        # 방문 목록
        visited = [-1 for _ in range(N)]
        # 우선 경로 탐색 BFS
        while dq:  
            # 싱크에 도달했으면
            if 1 in dq:
                break
            # 현재 노드
            now_node = dq.popleft()
            # 이동 가능한 노드 탐색
            for node in graph[now_node]:
                # 방문한 적 없고 이동가능한 유량이 남아있으면
                if visited[node] < 0 and flowable[now_node][node]:
                    # 방문 체크
                    visited[node] = now_node
                    # 데크에 추가
                    dq.append(node)

        # 싱크에 도달하지 못했으면
        if not dq:
            break
        
        # 경로 + 1
        cnt += 1
        # 경로 추적
        route = deque([1])
        while route[0] != 0:
            # 현재 노드
            now_node = route[0]
            # 이전 노드
            before_node = visited[now_node]
            # 경로 추가
            route.appendleft(before_node)
        
        # 경로 따라 유량 옮기기
        for i in range(len(route)-1):
            # 경로
            s = route[i]
            e = route[i+1]
            # 유량 옮기기
            liquid[s] -= 1
            liquid[e] += 1
            # 흐를수 있는 유량 업데이트
            flowable[s][e] -= 1
            flowable[e][s] += 1

    print(cnt)


# 입력
N, P = map(int, input().strip().split())
edges = [list(map(lambda x: int(x)-1, input().strip().split())) for _ in range(P)]

solution(N, P, edges)