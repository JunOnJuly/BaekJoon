import sys

input = sys.stdin.readline


def solution(N, liquides):
    # 투포인터
    l = 0
    r = N-1
    # 절댓값을 취할 시 최솟값이 되는 값
    min_state_value = liquides[r] + liquides[l]
    # 순회
    while l<r:
        # 상태값 갱신
        state_value = liquides[r] + liquides[l]
        # 최소 상태값 갱신
        if abs(state_value) < abs(min_state_value):
            min_state_value = state_value

        # 상태값이 0 이상이면
        if state_value > 0:
            # r 움직이기
            r -= 1
        
        # 0 이하면
        elif state_value < 0:
            # l 움직이기
            l += 1
        
        # 0 이면 그냥 출력
        else:
            print(0)
            return
        
    print(min_state_value)


# 입력
N = int(input().strip())
liquides = list(map(int, input().strip().split()))

solution(N, liquides)