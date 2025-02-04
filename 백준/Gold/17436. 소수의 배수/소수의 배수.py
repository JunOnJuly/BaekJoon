import sys
from itertools import combinations
from math import prod

input = sys.stdin.readline


def solution(N, M, primes):
    # 총 카운트
    total_cnt = 0
    # 소수 정렬
    primes = sorted(primes)
    # 조합 수 순회
    for i in range(1, N+1):
        # 조합 순회
        for comb in combinations(primes, i):
            # 배수의 수
            cnt = M//prod(comb)
            # 계산
            total_cnt += cnt if i%2 else -cnt
    
    print(total_cnt)


# 입력
N, M = map(int, input().strip().split())
primes = list(map(int, input().strip().split()))

solution(N, M, primes)