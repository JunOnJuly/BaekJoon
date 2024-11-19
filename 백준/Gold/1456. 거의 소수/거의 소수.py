import sys
import math

input = sys.stdin.readline


def soltuion(A, B):
    # 소수 판정 범위
    right = math.ceil(pow(B, 1/2))
    ## right 이하의 소수 찾기
    # 소수 판별 리스트
    is_primes = [False, False] + [True for _ in range(right-1)]
    # 소수
    primes = []
    # 순회
    for i in range(2, len(is_primes)):
        # 현재 수가 소수가 아니면 패스
        if not is_primes[i]:
            continue
    
        # 아니면 소수 판별 리스트 업데이트
        for j in range(2*i, len(is_primes), i):
            is_primes[j] = False
        
        # 소수 추가
        primes.append(i)
    
    # 거의 소수 카운트
    almost_prime_cnt = 0
    # 소수 순회하며 범위에 포함되는지 체크
    for prime in primes:
        for exp in range(2, int(math.log2(B))+1):
            # 거의 소수 후보
            candid_almost_prime = pow(prime, exp)
            # 범위에 포함되면 카운트 + 1
            if candid_almost_prime >= A and candid_almost_prime <= B:
                almost_prime_cnt += 1
            
            # B 를 초과하면 다음
            elif candid_almost_prime > B:
                break
    
    print(almost_prime_cnt)
    

# 입력
A, B = map(int, input().strip().split())

soltuion(A, B)