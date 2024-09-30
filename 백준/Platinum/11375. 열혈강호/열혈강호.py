import sys

input = sys.stdin.readline


# 이분매칭
def bimatch(idx, visited, connected, hope_list):
    # 방문했으면 패스
    if visited[idx]:
        return False
    # 방문
    visited[idx] = True

    # 담당할 수 있는 일 순회하며 확인
    for node in hope_list[idx]:
        # 담당할 수 있거나 배치된 사람을 옮길 수 있다면
        if not connected[node] or bimatch(connected[node], visited, connected, hope_list):
            # 담당
            connected[node] = idx
            return True
    
    return False
    

def solution(N, M, hope_list):
    # 담당한 일 리스트
    connected = [0 for _ in range(M+1)]
    # 순회
    for i in range(1, N+1):
        # 방문 목록
        visited = [False for _ in range(N+1)]
        # 이분매칭
        bimatch(i, visited, connected, hope_list)
    
    print(sum([1 for c in connected if c]))


# 입력
N, M = map(int, input().strip().split())
hope_list = [[]] + [list(map(int, input().strip().split()))[1:] for _ in range(N)]

solution(N, M, hope_list)