import sys

input = sys.stdin.readline
      

def solution(n):
    ## 피사노 주기
    # 주기는 10^6 일 때 15 * (10^5)
    # n 주기로 나눠주기
    n %= 15*(pow(10, 5))
    # DP
    memo = [0, 1]
    # 순회
    for i in range(2, n+1):
        memo.append((memo[i-1] + memo[i-2])%1000000)
    
    print(memo[n])


# 입력
n = int(input().strip())

solution(n)