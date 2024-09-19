import sys
from itertools import combinations_with_replacement
from math import sqrt

input = sys.stdin.readline


# N 이하의 소수 찾기
def find_unique(N):
    # 에라토스테네스의 체
    sieve = [1 for _ in range(N+1)]
    sieve[0] = 0
    sieve[1] = 0
    # 순회 범위
    root_N = int(sqrt(N))
    # 순회
    for num in range(2, root_N+1):
        # 체크되지 않은 수면
        if sieve[num]:
            for i in range(2*num, N+1, num):
                # 배수 모두 체크
                sieve[i] = 0
    
    # 체크되지 않은 수 리스트
    unqs = [i for i in range(len(sieve)) if sieve[i]]

    return unqs


def solution(N):
    # 골드바흐 추측에 의한 경우 분리
    # N 이 홀수면 N - K 가 짝수기 위해서는 K 는 홀수
    # -> 합이 가장 작은 홀수가 되는 소수 조합 = [2, 3]
    # N 이 짝수면 N - K 가 홀수기 위해서는 K 는 짝수
    # -> 합이 가장 작은 짝수가 되는 소수 조합 = [2, 2]
    # N 이 홀수면
    if N % 2:
        result = [2, 3]
        N -= 5
    # N 이 짝수면
    else:
        result = [2, 2]
        N -= 4
    # N 이하의 소수 리스트
    uniques = find_unique(N)
    # 조합
    for unqs in combinations_with_replacement(uniques, 2):
        # 조합의 합
        sum_unqs = sum(unqs)
        # 조합의 합이 N
        if sum_unqs == N:
            # 소수 리스트 최신화
            result.extend(unqs)
            return sorted(result)


# 입력
N = int(input().strip())
# N 이 8 미만이면 없음
if N < 8:
    print(-1)
else:
    result = solution(N)
    if result:
        print(*result)
    else: print(-1)