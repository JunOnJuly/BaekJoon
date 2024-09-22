import sys
from bisect import bisect_left

input = sys.stdin.readline


def solution(N):
    # N 보다 작은 육각수 리스트
    hex_list = [0]
    # 카운트
    i = 1
    j = 1
    while True:
        # N 이하면
        if i*j <= N:
            hex_list.append((i)*(j))
            i += 1
            j += 2
        # 크면 끝
        else:
            break

    # DP / memo[i] = i 를 만드는데 필요한 육각수의 최소 개수
    memo = [0]
    # 순회
    for i in range(1, N+1):
        # 1(i 이하인 육각수) + (i - (i 이하인 육각수)를 만드는데 필요한 육각수의 최소 개수))
        # 중 가장 작은값 찾기
        min_hex_cnt = float('inf')
        for j in range(1, len(hex_list)):
            # i 보다 크면 끝
            if hex_list[j] > i:
                break
            # 최솟값 최신화
            min_hex_cnt = min(min_hex_cnt, 1 + memo[i-hex_list[j]])
        # memo 최신화
        memo.append(min_hex_cnt)

    return memo[-1]

    
# 입력
N = int(input().strip())
print(solution(N))