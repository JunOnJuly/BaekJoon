def solution(N, data_list):
    # 인덱스 맞추기
    data_list = [[0, 0, 0, 0]] + data_list
    # 시스템 상 최댓값
    inf = 1000001
    # 2차원 DP
    # 첫 선택에 따라 최솟값이 달라지므로
    # R, G, B 세 개로 나눠야 한다
    memo_R = [[0 for _ in range(4)] for __ in range(N+1)]
    memo_G = [[0 for _ in range(4)] for __ in range(N+1)]
    memo_B = [[0 for _ in range(4)] for __ in range(N+1)]
    # 초깃값 설정
    memo_R[1] = [0, data_list[1][1], inf, inf]
    memo_G[1] = [0, inf, data_list[1][2], inf]
    memo_B[1] = [0, inf, inf, data_list[1][3]]
    
    # 메모 최신화
    for i in range(2, N+1):
        for j in range(1, 4):
            memo_R[i][j] = min([memo_R[i-1][k] if k != j else inf for k in range(1, 4)]) + data_list[i][j]
            memo_G[i][j] = min([memo_G[i-1][k] if k != j else inf for k in range(1, 4)]) + data_list[i][j]
            memo_B[i][j] = min([memo_B[i-1][k] if k != j else inf for k in range(1, 4)]) + data_list[i][j]
    # 각 초깃값에 따른 최솟값
    min_R = min(memo_R[-1][1:])
    min_G = min(memo_G[-1][1:])
    min_B = min(memo_B[-1][1:])

    return min(min_R, min_G, min_B)


N = int(input())
data_list = [[0] + list(map(int, input().split())) for _ in range(N)]
print(solution(N, data_list))