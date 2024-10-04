import sys

input = sys.stdin.readline


# 이분매칭
def bimatch(idx, connectable, visited, connected):
    # 이미 체크한 수이면
    if visited[idx]:
        return False
    # 체크
    visited[idx] = True
    # 연결될 수 있는 수 목록 순회
    for node in connectable[idx]:
        # 연결될 수 있는 수 이거나 다른 수와 연결할 수 있으면
        if connected[node] < 0 or bimatch(connected[node], connectable, visited, connected):
            # 연결
            connected[node] = idx
            # 잡아먹힌 상어는 잡아먹을 수 없음
            visited[node] = True
            return True
    return False


def solution(N, state_list):
    # 연결 가능한 목록
    connectable = [[] for _ in range(N)]
    # 순회하며 연결 가능한 목록 만들기
    for i in range(N-1):
        for j in range(i+1, N):
            # 잡아먹을 수 있으면
            if all([state_list[i][idx] >= state_list[j][idx] for idx in range(3)]):
                connectable[i].append(j)
            elif all([state_list[i][idx] <= state_list[j][idx] for idx in range(3)]):
                connectable[j].append(i)

    # 연결 목록
    connected = [-1 for _ in range(N)]
    # 순회하며 이분매칭
    for idx in range(N):
        # 두 마리까지 먹을 수 있음
        for _ in range(2):
            # 방문목록
            visited = [False for _ in range(N)]
            # 이분매칭
            bimatch(idx, connectable, visited, connected)

    print(sum([1 for c in connected if c < 0]))


# 입력
N = int(input().strip())
state_list = [list(map(int, input().strip().split())) for _ in range(N)]

solution(N, state_list)