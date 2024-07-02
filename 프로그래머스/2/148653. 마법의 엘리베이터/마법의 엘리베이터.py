from collections import deque


def solution(storey):
    # n 번째 자리의 수를 판단하고 가까운 쪽으로 채우는 방향으로 이동
    n = -1
    # 카운트
    cnt = 0
    # 순회
    while storey != 0:
        # n 번째 자리까지 반올림
        temp = storey
        storey = round(storey, n)
        n -= 1
        # 카운트 추가
        cnt += abs(temp - storey) / pow(10, abs(n) - 2)
        
    return cnt