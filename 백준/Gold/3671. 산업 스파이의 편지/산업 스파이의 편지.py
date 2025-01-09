import sys
from itertools import permutations

input = sys.stdin.readline

    
def solution(c, nums):
    # 7자리 이하 소수 모두 구하기
    limit = 10000000
    # 소수 판정 리스트
    is_prime = [1 for _ in range(limit+1)]
    is_prime[0] = 0
    is_prime[1] = 0
    # 순회
    for num in range(int(pow(len(is_prime), 1/2))+1):
        # 해당 수가 소수면
        if is_prime[num]:
            # 배수 모두 소수가 아님
            for n in range(2*num, len(is_prime), num):
                is_prime[n] = 0

    # 수 조합
    for n in nums:
        # 조합된 수 셋
        c_nums = set()
        # 조합할 수 개수
        for i in range(1, len(n)+1):
            for c_n in permutations(n, i):
                # 조합된 수
                c_nums.add(int(''.join(c_n)))

        print(sum([1 for num in c_nums if is_prime[num]]))


# 입력
c = int(input().strip())
nums = [input().strip() for _ in range(c)]

solution(c, nums)