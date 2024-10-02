import sys

input = sys.stdin.readline


# 이분매칭
def bimatch(idx, hope_list, visited, connected):
    # 이미 체크한 사람이면
    if visited[idx]:
        return False
    # 체크
    visited[idx] = True
    # 원하는 책 목록 순회
    for node in hope_list[idx]:
        # 체크할 수 있는 사람이거나 다른 사람에게 책을 줄 수 있는 사람이면
        if not connected[node] or bimatch(connected[node], hope_list, visited, connected):
            # 책 주기
            connected[node] = idx
            return True
        
    return False


def solution(N, M, hope_list):
    # 이분매칭
    # 매칭 목록
    connected = [0 for _ in range(N+1)]
    # 사람 순회하며 원하는 책을 얻을수 있는지 확인
    for idx in range(1, M+1):
        # 방문 목록
        visited = [False for _ in range(M+1)]
        # 이분매칭
        bimatch(idx, hope_list, visited, connected)
    
    print(sum([1 for c in connected if c]))


# 입력
T = int(input().strip())
for _ in range(T):
    N, M = map(int, input().strip().split())
    hope_list = [[]]
    for m in range(M):
        a, b = map(int, input().strip().split())
        hope_list.append(list(range(a, b+1)))

    solution(N, M, hope_list)