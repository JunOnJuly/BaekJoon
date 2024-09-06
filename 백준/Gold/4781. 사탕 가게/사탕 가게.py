import sys
input = sys.stdin.readline


def solution(data_list):
    # 데이터 길이
    n = len(data_list)
    # 냅색 알고리즘
    knapsack = [0 for _ in range(m+1)]
    # 큰 금액부터순회
    for i in range(m+1):
        # 데이터 순회
        for j in range(n):
            if data_list[j][1] <= i:
                knapsack[i] = max(knapsack[i], knapsack[i-data_list[j][1]] + data_list[j][0])

    return knapsack[-1]


# 입력
while True:
    n, m = map(float, input().strip().split())
    if not n:
        break
    n = int(n)
    m = int(m*100)

    data_list = []
    for _ in range(n):
        c, p = map(float, input().strip().split())
        c = int(c)
        p = int(p*100 + 0.5)
        data_list.append([c, p])

    print(solution(data_list))