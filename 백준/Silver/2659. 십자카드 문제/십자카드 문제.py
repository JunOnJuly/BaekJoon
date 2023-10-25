def solution(card):
    clock_num = find_min(card)
    return count_min(clock_num)


# 시계수 찾기
def find_min(card):
    min_card = int(card)
    # 카드 돌리면서 최솟값 찾기
    for _ in range(3):
        card = card[1:] + card[:1]
        if min_card > int(card):
            min_card = int(card)

    return min_card


# 시계수 순서 찾기
def count_min(clock_num):
    cnt = 1
    for i in range(1, 10):
        for j in range(1, 10):
            for k in range(1, 10):
                for l in range(1, 10):
                    temp_num = f'{i}{j}{k}{l}'
                    if temp_num == str(clock_num):
                        return cnt
                    if str(find_min(temp_num)) == temp_num:
                        cnt += 1
    
    return cnt


card = ''.join(input().split())
print(solution(card))