import sys


def solution(N, data_list):
    # 데이터 정렬
    data_list = sorted(data_list)
    # 투포인터
    left = 0
    right = N-1
    # 비교 값
    value = int(2e9)
    # 포인터 값
    left_value = data_list[left]
    right_value = data_list[right]
    # 탐색
    while True:
        # 합
        sum_value = data_list[left] + data_list[right]
        # value 를 비교해 value, left_value, right_value 를 최신화
        if abs(sum_value) < value:
            value = abs(sum_value)
            left_value = data_list[left]
            right_value = data_list[right]
        # 포인터 이동
        # 0 보다 크면 합이 작아져야 하므로 right 이동
        if sum_value > 0:
            right -= 1
        # 0 보다 작으면 left 이동
        elif sum_value < 0:
            left += 1
        # 포인터가 겹치거나 합이 0이면 끝
        if left >= right or value == 0:
            print(f'{left_value} {right_value}')
            return


N = int(sys.stdin.readline().strip())
data_list = list(map(int, sys.stdin.readline().strip().split()))
solution(N, data_list)