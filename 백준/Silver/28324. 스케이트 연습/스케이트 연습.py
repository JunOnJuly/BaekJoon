import sys

input = sys.stdin.readline


def solution(N, limits):
    # limits 반전
    limits = list(reversed(limits))
    # 속도 총 합
    v_sum = 0
    # 현재 속도
    now_v = 0
    # 순회
    for limit in limits:
        # 현재 속도 + 1 이 제한 이하면 
        if now_v + 1 <= limit:
            # 올리기
            now_v += 1
        
        # 제한 초과면
        else:
            # 한계치까지 내림
            now_v = limit

        # 속도 합
        v_sum += now_v
    
    print(v_sum)


# 입력
N = int(input().strip())
limits = list(map(int, input().strip().split()))

solution(N, limits)