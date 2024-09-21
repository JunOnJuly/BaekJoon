import sys

input = sys.stdin.readline


def solution(N):
    # DP / memo[i][j] = 자릿수가 i 이고 첫 숫자가 j 인 줄어드는 수의 개수
    memo = [[0 for _ in range(11)] for _ in range(11)]
    for i in range(10):
        memo[1][i] = 1
    # 자릿수가 K 인 줄어드는 수의 개수 = 
    # 자릿수가 K - 1 이고 첫 숫자가 K 번째 올 수보다 작은 모든 경우의 수
    
    # 순회
    # 자릿수
    for i in range(2, 11):
        # 맨 앞에 오는 수
        for j in range(1, 10):
            # 맨 앞에 오는 수가 자릿수 - 1 이상일때만
            if j >= i-1:
                # 점화식
                memo[i][j] = sum([memo[i-1][j_in] for j_in in range(len(memo[i-1])) if j_in < j])
    
    # 카운트 합
    cnt_sum = 0
    # 직전 카운트
    before_cnt_sum = 0
    # 자릿수
    digit = 0
    # 시작 숫자
    start_num = 0
    # memo 순회하며 자릿수 / 시작 숫자 탐색
    for i in range(1, 11):
        for j in range(10):
            # 카운트 누적
            cnt_sum += memo[i][j]
            # 카운트가 N 이상이면
            if cnt_sum >= N:
                # 자릿수 / 시작 숫자 기록
                digit = i
                start_num = j
                break
            # 직전 카운트 누적
            before_cnt_sum = cnt_sum

        # 자릿수와 시작 숫자가 정해졌으면 순회 끝
        if digit:
            break
    
    # 불가능한 N 이면
    if not digit:
        return -1
    
    # print(f'자릿수 : {digit}')
    # print(f'시작 숫자 : {start_num}')
    # print(f'직전 카운트 : {before_cnt_sum}')

    # 자릿수와 시작 숫자부터 시작
    num = ''.join([str(i) for i in range(digit-1, -1, -1)])
    num = str(start_num) + num[1:]
    num = int(num)

    # print(f'시작 수 : {num}')

    # 카운트
    cnt = before_cnt_sum + 1
    # 순회
    while cnt != N:
        # 수를 늘려가며 줄어드는 수인지 판단
        num += 1
        if all([str(num)[i] > str(num)[i+1] for i in range(digit-1)]):
            cnt += 1

    return num


# 입력
N = int(input().strip())
print(solution(N))