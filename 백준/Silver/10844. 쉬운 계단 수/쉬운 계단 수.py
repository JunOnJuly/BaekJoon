def solution(N):
    # DP
    # 열은 자릿수
    # 행은 자릿수에 들어가는 숫자
    memo = [[0 for _ in range(N+1)] for _ in range(10)]
    # 1자리는 0 빼고 다 1 이니까 채워주기
    for i in range(1, 10):
        memo[i][1] = 1
    # n+1 번째 자리에서 n 번째 자리를 고려하면
    # n+1 번째 자리가 0일 경우 2 한 가지
    # n+1 번째 자리가 9일경우 8 한 가지
    # 나머지는 +- 1 한 2가지가 나오는 것을 알 수 있다
    # 즉 memo[m][n+1] = memo[m-1][n] + memo[m+1][n] if 0<m<9
    #    memo[m][n+1] = memo[m-1][n] if m==9
    #    memo[m][n+1] = memo[m+1][n] if m==0
    for j in range(2, N+1):
        for i in range(0, 10):
            if i == 0:
                memo[i][j] = memo[i+1][j-1]
            elif i == 9:
                memo[i][j] = memo[i-1][j-1]
            else:
                memo[i][j] = memo[i-1][j-1] + memo[i+1][j-1]


    return sum([memo[i][-1] for i in range(10)]) % 1000000000


N = int(input())
print(solution(N))
