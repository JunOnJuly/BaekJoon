import sys
from itertools import combinations

input = sys.stdin.readline


def solution(L, C, chr):
    # 조합
    for comb in combinations(chr, L):
        # 한 개의 모음과 두 개의 자음
        m = 0
        j = 0
        for c in comb:
            if c in 'aeiou':
                m += 1
            else:
                j += 1
        
        if m and j >= 2:
            print(''.join(comb))


# 입력
L, C = map(int, input().strip().split())
chr = ''.join(sorted(input().strip().split()))

solution(L, C, chr)