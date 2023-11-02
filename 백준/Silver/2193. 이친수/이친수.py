def solution(n):
    # DP
    memo = [0 for _ in range(91)]
    # 앞 부분 미리 작성
    memo[1] = 1
    memo[2] = 1

    i = 3
    while True:
        # 중단 조건
        if i >= n+1:
            return memo[n]
        # 맨 앞은 10 으로 고정되어 있음
        # 그 뒤를 생각해야 하는데, 시작이 1 인 경우와 0 인 경우로 나누어 생각해보자
        # 시작이 1 인 경우는 단순히 n-2 자릿수를 가진 이친수와 같은 경우의 수를 가진다
        # 시작이 0인 경우는 맨 앞이 1, 다음이 0 으로 고정되어 있다는 점을 생각해보면
        # n-1 자릿수를 가진 이친수와 같은 경우의 수를 가진다는 것을 알 수 있다
        # 즉 f(n) = f(n-1) + f(n-2) 이다
        memo[i] = memo[i-1] + memo[i-2]
        i += 1


n = int(input())
print(solution(n))