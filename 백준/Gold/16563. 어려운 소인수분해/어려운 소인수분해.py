import sys

input = sys.stdin.readline


# 소인수 분해
def make_prime_factors(k, memo, primes):
    # k 의 소인수가 기록되어 있다면
    if memo[k]:
        # 소인수 리턴
        return memo[k]
    
    # 소수 순회
    for p in range(len(primes)):
        # 소수
        prime = primes[p]
        # 소수로 나누어떨어지면
        if not k%prime:
            # 기록
            memo[k].append(prime)
            # 재귀
            memo[k].extend(make_prime_factors(k//prime, memo, primes))
            # 리턴
            return memo[k]

        # 모든 소수로 나누어 떨어지지 않으면 자신이 소수
        elif p == len(primes)-1:
            # 기록
            memo[k].append(k)
            # 리턴
            return memo[k]


def solution(N, ks):
    # 수 내림차순 정렬
    sorted_ks = sorted(ks, reverse=True)
    max_ks = sorted_ks[0]
    # 소수 판정 리스트
    is_prime = [1 for _ in range(int(pow(max_ks, 1/2))+1)]
    is_prime[0] = 0
    is_prime[1] = 0
    # 소수 리스트
    primes = []
    # DP
    memo = [[] for _ in range(max_ks + 1)]
    # 순회
    for num in range(2, len(is_prime)):
        # 소수면
        if is_prime[num]:
            # 배수 모두 비소수 체크
            for non_prime in range(num*2, len(is_prime), num):
                is_prime[non_prime] = 0
            
            # 소수 리스트 추가
            primes.append(num)
            memo[num].append(num)
    
    # 순회하며 탐색 및 기록
    for k in sorted_ks:
        make_prime_factors(k, memo, primes)

    # 출력
    for k in ks:
        print(*sorted(memo[k]))


# 입력
N = int(input().strip())
ks = list(map(int, input().strip().split()))

solution(N, ks)