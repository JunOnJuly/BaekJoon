import sys

input = sys.stdin.readline


def seq(num):
    # 카운트
    div_cnt = 0
    sub_cnt = 0
    # 순회
    while num:
        # 2 로 나누어 떨어지면
        if not num%2:
            num //= 2
            div_cnt += 1
        
        # 나누어떨어지지 않으면
        else:
            num -= 1
            sub_cnt += 1

    return div_cnt, sub_cnt


def solution(N, B):
    # 각 배열의 원소를 -1 과 //2 로 0 으로 바꾸는 횟수
    for b in range(len(B)):
        B[b] = seq(B[b])
    
    # 뺀 횟수는 모두 더하고 나눈 횟수는 최댓값만 사용
    cnt = sum([s for d, s in B]) + max([d for d, s in B])
    
    print(cnt)


# 입력
N = int(input().strip())
B = list(map(int, input().strip().split()))

solution(N, B)