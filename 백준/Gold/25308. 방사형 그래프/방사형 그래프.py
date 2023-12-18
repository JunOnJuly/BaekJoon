from itertools import permutations
import math


def solution(data_list):
    # 데이터를 조합
    permute_data = permutations(data_list, 8)
    # 카운트
    count_convex = 0
    # 인덱스를 돌아가면서 판단
    for data in permute_data:
        for idx in range(8):
            if not cal_deg(data, idx):
                break
            elif idx == 7:
                count_convex += 1
    print(count_convex)


# 특정 인덱스의 볼록을 판단하는 함수
def cal_deg(data_list, idx):
    # 양 옆 인덱스
    left_idx = idx-1
    right_idx = (idx+1)%8
    # 왼쪽 밑변
    left_bottom = ((1/math.sqrt(2))*data_list[left_idx]) - data_list[idx]
    # 왼쪽 높이
    left_height = (1/math.sqrt(2))*data_list[left_idx]
    # 왼쪽 각도
    left_deg = math.degrees(math.atan(left_height/left_bottom))
    if left_deg < 0:
        left_deg += 180
    # 오른쪽 밑변
    right_bottom = ((1/math.sqrt(2))*data_list[right_idx]) - data_list[idx]
    # 오른쪽 높이
    right_height = (1/math.sqrt(2))*data_list[right_idx]
    # 오른쪽 각도
    right_deg = math.degrees(math.atan(right_height/right_bottom))
    if right_deg < 0:
        right_deg += 180
    # 오른쪽 각도와 왼쪽 각도의 합이 180 보다 작으면 오목
    if left_deg + right_deg < 180:
        return False
    else:
        return True


data_list = list(map(int, input().split()))
solution(data_list)