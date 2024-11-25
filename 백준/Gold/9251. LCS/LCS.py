import sys

input = sys.stdin.readline


def solution(strs):
    # DP 맵
    memo = [[0 for _ in range(len(strs[1])+1)] for __ in range(len(strs[0])+1)]
    # 탐색
    for i in range(1, len(memo)):
        for j in range(1, len(memo[0])):
            # 문자가 같으면
            if strs[0][i-1] == strs[1][j-1]:
                # 최대 공통 문자열 값 + 1
                memo[i][j] = memo[i-1][j-1] + 1
            
            # 문자가 다르면
            else:
                # 이전 문자들 중 최대 공통 문자열 값
                memo[i][j] = max(memo[i-1][j], memo[i][j-1])

    print(memo[-1][-1])


# 입력
strs = [input().strip() for _ in range(2)]

solution(strs)