import sys
from bisect import insort

input = sys.stdin.readline


def solution(M, data_list):
    # 결과 리스트
    result = []
    # 하나씩 데이터를 넣을 리스트
    input_list = []
    # 하나씩 데이터를 넣기
    for i in range(M):
        insort(input_list, data_list[i])
        # 홀수면
        if not i%2:
            # 중앙값 넣기
            result.append(input_list[i//2])

    return result


# 입력
T = int(input().strip())
for _ in range(T):
    M = int(input().strip())
    data_list = []
    for __ in range(M//10 + 1):
        data_list += list(map(int, input().strip().split()))
    
    result = solution(M, data_list)
    print(len(result))
    for i in range(0, len(result), 10):
        print(*result[i:i+10])