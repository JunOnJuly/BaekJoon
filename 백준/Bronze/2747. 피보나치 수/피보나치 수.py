import sys

input = sys.stdin.readline
      

def solution(n):
    # DP
    memo = [0, 1]
    # 순회
    for i in range(2, n+1):
        memo.append(memo[i-1] + memo[i-2])
    
    print(memo[n])


# 입력
n = int(input().strip())

solution(n)