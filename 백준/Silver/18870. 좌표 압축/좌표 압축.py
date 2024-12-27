import sys
from collections import defaultdict

input = sys.stdin.readline


def solution(N, nums):
    # 중복 수 제거
    comp_nums = list(set(nums))
    # 정렬
    comp_nums = sorted(comp_nums)
    # 순회하며 압축
    comp_dict = defaultdict(int)
    for i in range(len(comp_nums)):
        comp_dict[comp_nums[i]] = i
    
    print(*[comp_dict[num] for num in nums])

    
# 입력
N = int(input().strip())
nums = list(map(int, input().strip().split()))

solution(N, nums)