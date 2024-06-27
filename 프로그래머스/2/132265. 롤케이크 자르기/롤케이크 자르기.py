from collections import Counter, deque


def solution(topping):
    # 데크로 치환
    topping = deque(topping)
    # 카운트
    count_topping = Counter(topping)
    # 옮길 셋
    move_set = set()
    # 일치하는 수
    cnt = 0
    # 하나씩 순회하며 옮기기
    while topping:
        # 옮기기
        move_num = topping.popleft()
        move_set.add(move_num)
        # 카운트 최신화
        count_topping[move_num] -= 1
        if count_topping[move_num] == 0:
            del count_topping[move_num]
        # 셋과 카운트의 수 비교
        if len(move_set) == len(count_topping):
            cnt += 1
    
    return cnt