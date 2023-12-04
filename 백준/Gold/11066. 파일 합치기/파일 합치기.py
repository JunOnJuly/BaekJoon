import sys
from collections import deque


def solution(K, data_list):
    # data_list 를 어디서 끊어낼지 정하는 문제
    # i~j, j~k 까지 끊어낸 합 중 최대를 구하면 됨
    # DP, memo[i][j] 는 i 에서 j 까지 최소 코스트
    # memo[i][i] 는 0
    memo = [[1e9 for _ in range(K)] for __ in range(K)]
    for idx in range(K):
        memo[idx][idx] = 0
    # 누적합
    subsum = [0] + data_list
    for idx in range(len(subsum)):
        if idx:
            subsum[idx] += subsum[idx-1]
    # i~j 까지의 길이

    for i in range(2, K+1):
        # 시작하는 지점
        for j in range(K-i+1):
            # 끊어지는 지점
            for k in range(j, j+i-1):
                # 비교
                # 예를들어 [1, 2, 3] 이면
                # [1], [2, 3] 으로 끊는 것과
                # [1, 2], [3] 으로 끊는 것을 비교
                # 누적합을 더해주는 이유는 
                # [1], [2, 3] 인 경우
                # [1], [5] -> [6] 의 과정에서
                # 중간에 더해지는 코스트인 [2, 3] 을 더해주기 위함
                memo[j][j+i-1] = min(memo[j][j+i-1], memo[j][k] + memo[k+1][j+i-1] + subsum[j+i] - subsum[j])
    print(memo[0][K-1])


T = int(sys.stdin.readline().strip())
for _ in range(T):
    K = int(sys.stdin.readline().strip())
    data_list = list(map(int, sys.stdin.readline().strip().split()))
    solution(K, data_list)