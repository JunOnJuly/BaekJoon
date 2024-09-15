import sys

input = sys.stdin.readline


def solution(C, N, data_list):
    # 최대 비용 = 100 원에 1명씩 C 명을 모집할 경우 = 100xC 원
    max_cost = 100*C
    # 냅색
    knapsack = [[0 for _ in range(N)] for __ in range(max_cost+1)]
    # 직전 비용까지의 고객 수 최댓값
    # 현재 비용에서 필요 비용을 뺀 비용까지의 고객 수 최댓값 + 필요비용으로 얻은 고객
    # 중 최댓값 넣기
    for i in range(1, max_cost+1):
        for j in range(N):
            # 현재 비용이 필요 비용보다 클 때만
            if i >= data_list[j][0]:
                knapsack[i][j] = max(max(knapsack[i-1]), 
                                    max(knapsack[i-data_list[j][0]]) + data_list[j][1])

            # 목표 인원을 달성하면
            if knapsack[i][j] >= C:
                return i
                

# 입력
C, N = map(int, input().strip().split())
data_list = [list(map(int, input().strip().split())) for _ in range(N)]
print(solution(C, N, data_list))