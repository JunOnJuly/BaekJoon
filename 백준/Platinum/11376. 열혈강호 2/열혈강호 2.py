import sys

input = sys.stdin.readline


# 이분매칭
def bimatch(idx, visited, connected, hope_list):
    # 방문했으면 패스
    if visited[idx]:
        return False
    # 방문
    visited[idx] = True

    # 담당할 수 있는 사람 순회하며 확인
    for node in hope_list[idx]:
        # 해당 사람이 담당할 수 있는 첫 번째 업무가 비었으면
        if not connected[node][0]:
            # 담당
            connected[node][0] = idx
            return True
        # 해당 사람이 담당할 수 있는 두 번째 업무가 비었으면
        elif not connected[node][1]:
            # 담당
            connected[node][1] = idx
            return True
        # 담당하고 있는 첫 번째 업무를 다른 사람에게 옮길 수 있다면
        elif bimatch(connected[node][0], visited, connected, hope_list):
            # 담당
            connected[node][0] = idx
            return True
        # 담당하고 있는 두 번째 업무를 다른 사람에게 옮길 수 있다면
        elif bimatch(connected[node][1], visited, connected, hope_list):
            # 담당
            connected[node][1] = idx
            return True
    
    return False
    

def solution(N, M, hope_list):
    # 담당한 일 리스트
    # 일 -> 사람으로 매칭
    # hope list 반대로 재구성
    reverse_hope_list = [[] for _ in range(M+1)]
    for idx in range(len(hope_list)):
        for idx_n in hope_list[idx]:
            reverse_hope_list[idx_n].append(idx)
        
    connected = [[0, 0] for _ in range(N+1)]
    # 순회
    for i in range(1, M+1):
        # 방문 목록
        visited = [False for _ in range(M+1)]
        # 이분매칭
        bimatch(i, visited, connected, reverse_hope_list)
    
    print(sum([2-c.count(0) for c in connected]))


# 입력
N, M = map(int, input().strip().split())
hope_list = [[]] + [list(map(int, input().strip().split()))[1:] for _ in range(N)]

solution(N, M, hope_list)