from collections import deque
from copy import deepcopy


def solution(N, M, data_list):
    # 왼쪽으로만 이동하는 큐
    queue_left = deque(list(range(N)))
    # 오른쪽으로만 이동하는 큐
    queue_right = deque(list(range(N)))
    # 카운팅
    cnt = 0
    # 데이터 인덱스
    data_idx = 0
    # 이동 횟수
    move_cnt = 0
    # 시뮬레이션
    while True:
        # data_list 모두 순회하면 끝
        if data_idx == M:
            return cnt
        # 첫 원소가 data 면
        if queue_left[0] == data_list[data_idx]-1:
            # popleft
            queue_left.popleft()
            # queue 들 현 상태로 변환
            queue_right = deepcopy(queue_left)
            # 카운트 +
            cnt += move_cnt
            # 데이터 인덱스 + 1
            data_idx += 1
            # 이동 횟수 초기화
            move_cnt = 0
        # 첫 원소가 data 면
        elif queue_right[0] == data_list[data_idx]-1:
            # popleft
            queue_right.popleft()
            # queue 들 현 상태로 변환
            queue_left = deepcopy(queue_right)
            # 카운트 +
            cnt += move_cnt
            # 데이터 인덱스 + 1
            data_idx += 1
            # 이동 횟수 초기화
            move_cnt = 0
        # 둘 다 아니면
        else:
            # 각 방향으로 이동
            queue_left.append(queue_left.popleft())
            queue_right.appendleft(queue_right.pop())
            # 이동횟수 + 1
            move_cnt += 1


N, M = map(int, input().split())
data_list = list(map(int, input().split()))
print(solution(N, M, data_list))