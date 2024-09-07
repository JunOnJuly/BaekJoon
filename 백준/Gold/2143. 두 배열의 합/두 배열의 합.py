import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline


def solution(n, m, A, B):
    # 결과
    result = 0
    # 부분합 리스트로 치환
    A = [0] + A
    for i in range(1, n+1):
        A[i] += A[i-1]
    B = [0] + B
    for i in range(1, m+1):
        B[i] += B[i-1]
    # 모든 부분합 기록
    # bisect.insort 를 사용하면 쉽게 정렬할 수 있지만
    # 여러번 사용하면 효율이 떨어짐
    # 그냥 다 넣고 마지막에 정렬
    A_subsums = []
    for i in range(0, n):
        for j in range(i+1, n+1):
            A_subsums.append(A[j]-A[i])
    A_subsums.sort()
    B_subsums = []
    for i in range(0, m):
        for j in range(i+1, m+1):
            B_subsums.append(B[j]-B[i])
    B_subsums.sort()
    # A_subsum 을 탐색하며 A 부배열 합 정하기
    i = 0
    while i < len(A_subsums):
        # A 부배열 합
        A_sumsub = A_subsums[i]
        # A 부배열 합과 같은 수 다음 인덱스 검색
        same_A_sumsub = bisect_right(A_subsums, A_sumsub)
        # A 부배열 합과 같은 수 개수
        num_same_A_sumsub = same_A_sumsub - i
        # B 부배열 합
        B_sumsub = T-A_sumsub
        # B 부배열 합과 같은 수 검색
        same_B_sumsub_start = bisect_left(B_subsums, B_sumsub)
        same_B_sumsub_end = bisect_right(B_subsums, B_sumsub)
        num_same_B_sumsub = same_B_sumsub_end - same_B_sumsub_start
        # 결과에 더하기
        result += num_same_A_sumsub * num_same_B_sumsub     
        # i 를 뒤로 이동
        i = same_A_sumsub

    return result


# 입력
T = int(input().strip())
n = int(input().strip())
A = list(map(int, input().strip().split()))
m = int(input().strip())
B = list(map(int, input().strip().split()))

print(solution(n, m, A, B))