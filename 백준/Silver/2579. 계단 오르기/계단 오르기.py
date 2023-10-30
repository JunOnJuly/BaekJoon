def solution(N, data_list):
    # memo 와 자릿수 맞추기
    data_list = [0] + data_list
    # DP
    # 2 까지는 미리 채우기
    memo = [0 for _ in range(N+1)]
    memo[1] = data_list[1]
    # N 이 1이면
    if N == 1:
        return memo[1]
    memo[2] = memo[1] + data_list[2]
    # N 이 2면
    if N == 2:
        return memo[2]

    for i in range(3, N+1):
        # 점화식
        memo[i] = max(memo[i-2], memo[i-3] + data_list[i-1]) + data_list[i]
    
    return memo[-1]


N = int(input())
data_list = [int(input()) for _ in range(N)]
print(solution(N, data_list))