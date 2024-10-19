import sys

input = sys.stdin.readline


# 이분매칭
def bimatch(idx, connectable, connected, visited):
    # 방문했다면 패스
    if visited[idx]:
        return False
    
    # 방문 체크
    visited[idx] = True
    # 순회
    for node in connectable[idx]:
        # 선택할 수 있거나 옮길 수 있으면
        if connected[node] < 0 or bimatch(connected[node], connectable, connected, visited):
            # 선택
            connected[node] = idx
            
            return True
    
    return False


def solution(N, M, table):
    # 이분매칭
    # 행 / 열 로 나누어야 하지만
    # 중간에 끊긴 부분이 있으므로
    # 끊긴 부분은 다른 행 / 열로 간주
    # [행 / 열] 목록
    rc_table = [[[-1, -1] for _ in range(M)] for __ in range(N)]
    # 순회하며 업데이트
    # 누적 행
    before_row = 0
    for n in range(N):
        # 직전 상태
        before_state = True
        for m in range(M):
            # 현재 구멍이 뚫려있으면
            if table[n][m] == '*':
                # 직전 상태가 구멍이 아니면
                if not before_state:
                    before_row += 1
                    
                # 행 업데이트
                rc_table[n][m][0] = before_row
                # 직전 상태 업데이트
                before_state = True

            # 현재 구멍이 안뚫려있으면
            else:
                # 직전 상태 업데이트
                before_state = False
        
        before_row += 1

    # 누적 열
    before_column = 0  
    for m in range(M):
        # 직전 상태
        before_state = True
        for n in range(N):
            # 현재 구멍이 뚫려있으면
            if table[n][m] == '*':
                # 직전 상태가 구멍이 아니면
                if not before_state:
                    before_column += 1
                    
                # 행 업데이트
                rc_table[n][m][1] = before_column
                # 직전 상태 업데이트
                before_state = True

            # 현재 구멍이 안뚫려있으면
            else:
                # 직전 상태 업데이트
                before_state = False

        before_column += 1

    # 행 / 열 최댓값
    max_row = max([rc_table[n][m][0] for m in range(M) for n in range(N)])
    max_column = max([rc_table[n][m][1] for m in range(M) for n in range(N)])

    # 연결되어 있는 행 -> 열
    connectable = [[] for _ in range(max_row+1)]
    for n in range(N):
        for m in range(M):
            # 구멍이면
            if table[n][m] == '*':
                # 추가
                connectable[rc_table[n][m][0]].append(rc_table[n][m][1])
    
    # 선택한 위치
    connected = [-1 for _ in range(max_column+1)]
    # 순회
    for idx in range(max_row+1):
        # 방문목록
        visited = [False for _ in range(max_row+1)]
        # 이분매칭
        bimatch(idx, connectable, connected, visited)
    
    # 매칭된 수 리턴
    print(sum([1 for c in connected if c >= 0]))


# 입력
N, M = map(int, input().strip().split())
table = [input().strip() for _ in range(N)]

solution(N, M, table)