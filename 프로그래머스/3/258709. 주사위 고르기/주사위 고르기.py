from itertools import combinations, product
from bisect import bisect_left


def solution(dice):
    # 주사위의 개수
    n = len(dice)
    # 주사위들의 경우의 수
    dices_case = list(product(range(6), repeat=n//2))
    # 가장 확률이 높은 경우의 이긴 경우의 수
    max_win_cnt = 0
    # 의 경우 A 의 주사위 번호
    win_A = None
    # 모든 경우의 수
    for A in combinations(range(n), n//2):
        # B
        B = sorted(list(set(range(n))-set(A)))
        # 주사위의 합들
        sum_As = sorted([sum([dice[a][i] for a, i in zip(A, c)]) for c in dices_case])
        sum_Bs = sorted([sum([dice[b][i] for b, i in zip(B, c)]) for c in dices_case])
        # 이긴 경우의 수
        win_cnt = 0
        # 이긴 경우의 수 구해주기
        for a in sum_As:
            win_cnt += bisect_left(sum_Bs, a)
        # 최대 이긴 수 업데이트
        if win_cnt > max_win_cnt:
            max_win_cnt = win_cnt
            win_A = A
    
    return list(map(lambda x: x+1, list(win_A)))
        