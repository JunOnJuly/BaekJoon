import sys

input = sys.stdin.readline


def solution(N, nums):
    # DP / 0 행은 증가 / 1 행은 감소 부분수열
    memo = [[0 for _ in range(N)] for _ in range(2)]
    # 첫 번째 수는 무조건 바이토닉 수열
    memo[0][0] = 1
    memo[1][-1] = 1
    # 뒤집힌 수열
    rev_nums = list(reversed(nums))
    # 순회
    for i in range(1, N):
        ## 양 끝에서 시작
        # 부분 증가 수열
        memo[0][i] = max([0] + [memo[0][j] for j in range(i) if nums[j] < nums[i]]) + 1
        # 부분 증가 수열 (뒤에서 부터)
        memo[1][-i-1] = max([0] + [memo[1][j] for j in range(N-1, N-1-i, -1) if nums[j] < nums[-i-1]]) + 1

    # 0 행과 1 행을 병합
    memo = [m1 + m2 for m1, m2 in zip(memo[0], memo[1])]
    
    print(max(memo) - 1)


# 입력
N = int(input().strip())
nums = list(map(int, input().strip().split()))

solution(N, nums)