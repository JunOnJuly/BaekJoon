import sys
input = sys.stdin.readline


# solution
def solution(N):
    # 나누는 수
    div = 1000000007
    # 결과
    result = 1

    # 순회하며 곱
    for i in range(1, N, 2):
        result *= i
        result %= div

    return int(result)


N = int(input().strip())
print(solution(N))