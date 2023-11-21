from collections import deque


def solution(gear_list, K, data_list):
    # 데큐로 치환
    gear_list = [deque(gear) for gear in gear_list]
    # 데이터 리스트 순회
    for data in data_list:
        # gear_list 최신화
        gear_list = rotate_gear(gear_list, data)
    # 점수
    score = 0
    # 순회하며 점수 합산
    for idx, gear in enumerate(gear_list):
        if gear[0]:
            score += 2**(idx)
    
    return score


# 기어를 회전시키는 함수
def rotate_gear(gear_list, data):
    # 회전 방향과 기어 순서를 받아서 회전
    gear_num, dir = data
    # 회전 방향을 체크하는 리스트
    rotate_list = gear_to_rotate(gear_list, gear_num, dir)
    # 리스트를 참고하며 회전
    for idx, rotate in enumerate(rotate_list):
        # 현재 기어
        now_gear = gear_list[idx]
        # 시계방향 회전
        if rotate == 1:
            now_gear.appendleft(now_gear.pop())
        # 반시계방향 회전
        elif rotate == -1:
            now_gear.append(now_gear.popleft())
    return gear_list
            

# 회전 방향을 체크하는 함수
def gear_to_rotate(gear_list, gear_num, dir):
    # 투포인터
    left = gear_num-2
    right = gear_num
    # 돌릴 기어
    gear_to_rotate_list = [0, 0, 0, 0]
    gear_to_rotate_list[gear_num-1] = dir
    # 순회하며 돌릴 기어 체크
    while True:
        # 인덱스안에 포함되어 있으면
        if left >= 0 and left < 4:
            # 톱니가 맞물리면
            if gear_list[left][2] != gear_list[left+1][6]:
                # 오른쪽 톱니가 움직이지 않으면 같이 움직이지 않고
                # 움직인다면 반대로 움직임
                gear_to_rotate_list[left] = -gear_to_rotate_list[left+1]
            # 포인터 이동
            left -= 1
        # 인덱스안에 포함되어 있으면
        if right >= 0 and right < 4:
            # 톱니가 맞물리면
            if gear_list[right][6] != gear_list[right-1][2]:
                # 왼쪽 톱니가 움직이지 않으면 같이 움직이지 않고
                # 움직인다면 반대로 움직임
                gear_to_rotate_list[right] = -gear_to_rotate_list[right-1]
            # 포인터 이동
            right += 1
        # 모든 포인터가 인덱스를 벗어나면, 모두 탐색이 끝나면 끝
        if left < 0 and right >= 4:
            return gear_to_rotate_list


gear_list = [list(map(int, list(input()))) for _ in range(4)]
K = int(input())
data_list = [list(map(int, input().split())) for _ in range(K)]
print(solution(gear_list, K, data_list))