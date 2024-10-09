import sys
from math import sqrt

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


# 거리계산 함수
def cal_dist(rat_idx, cave_idx):
    rx, ry = rat_idx
    cx, cy = cave_idx

    return sqrt(pow(rx-cx, 2) + pow(ry-cy, 2))


def solution(N, M, S, V, rat_idxs, cave_idxs):
    # 들쥐가 들어갈 수 있는 땅굴들
    connectable = [[] for _ in range(N)]
    # 매가 내려오기 전에 도달할 수 있는 땅굴 계산
    for n in range(N):
        for m in range(M):
            # 들쥐와 땅굴의 거리 
            dist = cal_dist(rat_idxs[n], cave_idxs[m])
            # 들쥐가 땅굴까지 도달하는 시간
            time = dist/V
            # 매가 도달하는 시간보다 빠르면
            if time <= S:
                # 들어갈 수 있는 땅굴
                connectable[n].append(m)
    
    # 땅굴에 들어간 쥐 인덱스들
    connected = [-1 for _ in range(M)]
    # 순회
    for idx in range(N):
        # 방문 목록
        visited = [False for _ in range(N)]
        # 이분매칭
        bimatch(idx, connectable, connected, visited)
    
    # 땅굴에 들어가지 못한 수 리턴
    print(N - sum([1 for c in connected if c>=0]))
    
    
# 입력
N, M, S, V = map(int, input().strip().split())
rat_idxs = [list(map(float, input().strip().split())) for _ in range(N)]
cave_idxs = [list(map(float, input().strip().split())) for _ in range(M)]
solution(N, M, S, V, rat_idxs, cave_idxs)