def solution(n):
    # DP
    memo = [0 for _ in range(n+1)]
    # 2까지만 채우기
    memo[1] = 1
    if n == 1:
        return memo[1]
    memo[2] = 2

    # i 번째 맨 뒤가 = 모양이면
    # (i-2) 가지 이고
    # i 번째 맨 뒤가 | 모양이면
    # (i-1) 가지 이다.
    # 나머지를 셈하지 않는 이유는
    # 위의 경우의 수로 모두 조합할 수 있기 때문이다.
    # 즉 f(i) = f(i-2) + f(i-1) 이다.

    i = 3
    while True:
        # 종료 조건
        if i == n+1:
            return memo[-1] % 10007
        # 점화식
        memo[i] = memo[i-2] + memo[i-1]
        i += 1


n = int(input())
print(solution(n))