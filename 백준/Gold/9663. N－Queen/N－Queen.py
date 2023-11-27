import sys


# 인덱스에 배치 가능한지 판단하는 함수
def is_empty(row):
    # 가로는 할 필요 없음
    # 세로, 대각선
    for i in range(row):
        if queen[row] == queen[i] or abs(queen[i] - queen[row]) == abs(i - row):
            return False
    return True


# NQueen 재귀 함수
def n_queen(row):
    # 마지막 인덱스를 넘어가면
    if row == N:
        global cnt
        cnt += 1
        return
    else:
        # 인덱스를 돌며 탐색
        for i in range(N):
            # 인덱스에 퀸 배치
            queen[row] = i
            # 인덱스에 배치 가능하면
            if is_empty(row):
                # 재귀 호출
                n_queen(row+1)


N = int(sys.stdin.readline())
# 카운트
cnt = 0
# 퀸 인덱스
queen = [0] * N
# 함수 호출
n_queen(0)
print(cnt)