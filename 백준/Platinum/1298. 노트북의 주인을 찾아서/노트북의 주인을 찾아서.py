import sys
from collections import deque

input = sys.stdin.readline


# 이분 매칭
def bimatch(idx, visited, connected, bi_graph):
    # 방문했으면 패스
    if visited[idx]:
        return False
    # 방문 체크
    visited[idx] = True

    # 연결될 수 있는 노드 체크
    for node in bi_graph[idx]:
        # 연결되지 않았거나
        # 연결된 노드와 연결된 노드가 다른 노드를 선택할 수 있으면
        if not connected[node] or bimatch(connected[node], visited, connected, bi_graph):
            # 연결
            connected[node] = idx
            return True    
    return False


def solution(N, M, data_list):
    # 이분매칭을 위한 연결리스트 / 그래프
    connected = [0 for _ in range(N+1)]
    bi_graph = [[] for _ in range(N+1)]
    for a, b in data_list:
        bi_graph[a].append(b)
    # 한사람씩 순회
    for i in range(1, N+1):
        # 이분매칭을 위한 방문리스트
        visited = [False for _ in range(N+1)]
        # 이분매칭
        bimatch(i, visited, connected, bi_graph)
    # 연결 리스트에서 연결된 수 출력
    print(sum([1 for c in connected if c]))


# 입력
N, M = map(int, input().strip().split())
data_list = [list(map(int, input().strip().split())) for _ in range(M)]
solution(N, M, data_list)