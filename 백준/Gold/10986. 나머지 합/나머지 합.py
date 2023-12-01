import sys
from itertools import combinations


def solution(M, data_list):
    # 누적합
    subsum = 0
    # 구간합을 M 으로 나눈 나머지로 분류
    mod_list = [0 for _ in range(M)]
    for idx in range(len(data_list)):
        subsum += data_list[idx]
        mod_list[subsum%M] += 1
    # 카운트
    cnt = 0
    # 나머지가 0 인 경우는 우선 더함
    cnt += mod_list[0]
    # 차가 0 이 되는 경우를 조합해 콤비네이션 계산
    # -> mod_list 의 value 를 콤비네이션
    for idx in range(len(mod_list)):
        cnt += mod_list[idx] * (mod_list[idx]-1) // 2
    return cnt


N, M = map(int, sys.stdin.readline().split())
data_list = list(map(int, sys.stdin.readline().split()))
print(solution(M, data_list))