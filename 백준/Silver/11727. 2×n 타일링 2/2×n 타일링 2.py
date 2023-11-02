def solution(n):
    memo = [0 for _ in range(1001)]
    memo[1] = 1
    memo[2] = 3

    i = 3
    while True:
        # 종료조건
        if i >= n+1:
            return memo[n] % 10007
        # 타일링 1 의 사고방식에서 파생
        # 마지막이 = 인 경우는 ㅁ 인 경우의 수와 수가 같으므로
        # 두 배 해서 더해주면 끝
        
        # 점화식
        memo[i] = memo[i-1] + memo[i-2]*2
        i += 1


n = int(input())
print(solution(n))