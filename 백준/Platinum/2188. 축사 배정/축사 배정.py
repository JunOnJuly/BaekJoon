import sys
from collections import defaultdict

input = sys.stdin.readline


# 이분매칭
def bimatch(idx, visited, connected, hope_list):
    # 방문했으면 고려하지 않음
    if visited[idx]:
        return False
    # 방문체크
    visited[idx] = True

    # 열결될 수 있는 노드 체크
    for node in hope_list[idx]:
        # 연결되지 않았거나
        # 연결된 노드와 연결된 노드가 다른 노드를 선택할 수 있으면
        if not connected[node] or bimatch(connected[node], visited, connected, hope_list):
            # 연결
            connected[node] = idx
            return True
    return False
    

def solution(N, M, hope_list):
    # 축사에 배정받은 소
    connected = [0 for _ in range(M+1)]
    # 순회
    for i in range(1, N+1):
        # 방문 목록
        visited = [False for _ in range(N+1)]
        # 이분매칭
        bimatch(i, visited, connected, hope_list)
    
    print(sum([1 for con in connected if con]))


# 입력
N, M = map(int, input().strip().split())
hope_list = [[]] + [list(map(int, input().strip().split()))[1:] for _ in range(N)]

solution(N, M, hope_list)