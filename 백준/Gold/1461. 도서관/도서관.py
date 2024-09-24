import sys
from collections import deque
from bisect import bisect_right

input = sys.stdin.readline


def solution(N, M, data_list):
    # 이동 거리
    move_length = 0
    # 정렬
    data_list.sort()
    # 가장 멀리있는 인덱스
    far_idx = data_list[0] if abs(data_list[0]) >= abs(data_list[-1]) else data_list[-1]
    # 0 의 위치
    zero_idx = bisect_right(data_list, 0)
    # 0 을 기준으로 두개로 쪼개기 및 데크로 치환
    left_dq = deque(data_list[:zero_idx])
    right_dq = deque(data_list[zero_idx:])
    # 가장 먼 위치에서 M*K 번째 까지 회수
    for i in range(0, len(left_dq), M):
        move_length += -left_dq[i] * 2
    for i in range(len(right_dq)-1, -1, -M):
        move_length += right_dq[i] * 2
    # 가장 멀리있던 인덱스 빼주기
    move_length -= abs(far_idx)
    
    return move_length


# 입력
N, M = map(int, input().strip().split())
data_list = list(map(int, input().strip().split()))
print(solution(N, M, data_list))