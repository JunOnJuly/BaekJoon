import sys

input = sys.stdin.readline


# 2차원 부분 합 구하기
def subsum_2d(profits, left_top, right_bottom):
    # 전체범위 - 가로절반 - 세로절반 + 작은범위
    return (profits[right_bottom[0]][right_bottom[1]] -
            profits[right_bottom[0]][left_top[1]-1] -
            profits[left_top[0]-1][right_bottom[1]] +
            profits[left_top[0]-1][left_top[1]-1])


def solution(N, profits):
    # 부분합 리스트
    profits = [[0 for _ in range(N+1)]] + [[0] + profits[p] for p in range(N)]
    # 행 부분 합 리스트 계산
    for i in range(1, N+1):
        for j in range(1, N+1):
            profits[i][j] = profits[i][j] + profits[i][j-1]
    
    # 전체 부분 합 리스트 계산
    for j in range(1, N+1):
        for i in range(1, N+1):
            profits[i][j] = profits[i][j] + profits[i-1][j]

    # 방법의 수
    cnt = 0
    ## 특정 꼭짓점을 기준으로 네 방향을 계산
    # 꼭짓점 순회
    for i in range(N-1):
        for j in range(N-1):
            # 좌상단 리스트
            lts = [subsum_2d(profits, [k, l], [i+1, j+1]) for l in range(1, j+2) for k in range(1, i+2)]
            # 우하단
            rbs = [subsum_2d(profits, [i+2, j+2], [k, l]) for l in range(j+2, N+1) for k in range(i+2, N+1)]
            # 좌하단
            lbs = [subsum_2d(profits, [i+2, l], [k, j+1]) for l in range(1, j+2) for k in range(i+2, N+1)]
            # 우상단 
            rts = [subsum_2d(profits, [k, j+2], [i+1, l]) for l in range(j+2, N+1) for k in range(1, i+2)]
            # 좌상단 == 우하단
            for lt in lts:
                for rb in rbs:
                    if lt == rb:
                        # 카운트 + 1
                        cnt += 1
            
            # 좌하단 == 우상단
            for lb in lbs:
                for rt in rts:
                    if lb == rt:
                        # 카운트 + 1
                        cnt += 1

    print(cnt)


# 입력
N = int(input().strip())
profits = [list(map(int, input().strip().split())) for _ in range(N)]

solution(N, profits)