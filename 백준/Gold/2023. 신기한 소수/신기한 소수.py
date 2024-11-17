import sys

input = sys.stdin.readline


# 소수 판별
def is_prime(num):
    # 0, 1 이면 False
    if num in [0, 1]:
        return False
    
    # 소수 판별 리스트
    is_primes = [False, False] + [True for _ in range(int(pow(num, 1/2))-1)]
    # 순회
    for i in range(2, len(is_primes)):
        # 현재 수가 소수가 아니면 패스
        if not is_primes[i]:
            continue

        # 현재 수로 수가 나누어 떨어지면 소수가 아님
        if not num % i:
            return False
    
        # 아니면 소수 판별 리스트 업데이트
        for j in range(2*i, len(is_primes), i):
            is_primes[j] = False
    
    # 모두 통과하면 소수
    return True


def solution(N):
    # 신기한 소수 / amazing_primes[i] = [i 자릿수의 신기한 소수들]
    amazing_primes = [['']] + [[] for _ in range(N)]
    ## i-1 자리의 신기한 소수에 수를 붙여 소수면 추가
    # 순회
    for i in range(1, len(amazing_primes)):
        # i-1 자리의 신기한 소수
        for before_num in amazing_primes[i-1]:
            # 수 붙이기
            for num in range(10):
                # 소수 판정을 할 수
                now_num = int(before_num + str(num))
                # 소수 판정
                if is_prime(now_num):
                    # 신기한 소수 추가
                    amazing_primes[i].append(str(now_num))
    
    for amazing_prime in amazing_primes[N]:
        print(amazing_prime)


# 입력
N = int(input().strip())

solution(N)