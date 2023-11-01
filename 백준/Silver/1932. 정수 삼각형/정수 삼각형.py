def solution(n, data_list):
    # DP
    memo = [[0]*(i+1) for i in range(len(data_list))]
    # 최상단 채워주기
    memo[0][0] = data_list[0][0]
    # 아래로 내려가면서 더함
    # n 층에서 n+1 층으로 더함
    for i in range(n-1):
        for j in range(len(data_list[i])):
            # 같은 열과 +1열에 대해 메모와 합 비교
            for k in range(2):
                if memo[i+1][j+k] < memo[i][j] + data_list[i+1][j+k]:
                    memo[i+1][j+k] = memo[i][j] + data_list[i+1][j+k]
    
    return max(memo[-1])


n = int(input())
data_list = [list(map(int, input().split())) for _ in range(n)]
print(solution(n, data_list))