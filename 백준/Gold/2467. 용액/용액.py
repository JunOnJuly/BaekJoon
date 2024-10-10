import sys

input = sys.stdin.readline


def solution(fluids):
    ## 투포인터
    l = 0
    r = len(fluids)-1
    # 최소 절댓값
    min_abs_sum_nums = float('inf')
    # 합이 0 이거나 두 포인터가 교차할 때 까지
    while l < r:
        # 합
        sum_nums = fluids[l] + fluids[r]
        # 최소 절댓값 갱신
        if abs(sum_nums) < min_abs_sum_nums:
            min_abs_sum_nums = min(min_abs_sum_nums, abs(sum_nums))
            min_abs_nums = [fluids[l], fluids[r]]
        # 합이 0 보다 크면 r 값 조정
        if sum_nums > 0:
            r -= 1
        # 합이 0 보다 작으면 l 값 조정
        else:
            l += 1

    print(*min_abs_nums)

# 입력
N = int(input().strip())
fluids = list(map(int, input().strip().split()))
solution(fluids)