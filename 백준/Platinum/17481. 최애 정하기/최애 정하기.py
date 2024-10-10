import sys
from collections import defaultdict

input = sys.stdin.readline


# 이분매칭
def bimatch(idx, connectable, connected, visited):
    # 이미 방문한 노드면 탐색 안함
    if visited[idx]:
        return False
    # 방문 체크
    visited[idx] = True
    # 탐색 가능한 노드 탐색
    for node in connectable[idx]:
        # 연결할 수 있거나 연결된 노드를 다른 노드로 옮길 수 있다면
        if connected[node] < 0 or bimatch(connected[node], connectable, connected, visited):
            # 연결
            connected[node] = idx
            
            return True
        
    return False


def solution(N, M, connectable):
    # 해당 멤버를 좋아하는 친구
    connected = [-1 for _ in range(M)]
    # 순회
    for i in range(N):
        # 방문 목록
        visited = [False for _ in range(N)]
        # 이분매칭
        bimatch(i, connectable, connected, visited)
    
    sum_connected = sum([1 for c in connected if c >= 0])

    if sum_connected == N:
        print('YES')
    else:
        print('NO')
        print(sum_connected)

    
# 입력
N, M = map(int, input().strip().split())
names = defaultdict(int)
for i in range(M):
    names[input().strip()] = i
connectable = [list(map(lambda x: names[x], input().strip().split()[1:])) for _ in range(N)]

solution(N, M, connectable)