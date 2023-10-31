def solution(N, M, num_list, data_list):
    # 누적합 리스트 만들기
    sum_list = make_sum_list(N, num_list)
    # i ~ j 구간의 합은 (j 까지의 누적합) - (i-1 까지의 누적합)
    for i, j in data_list:
        print(sum_list[j] - sum_list[i-1])


def make_sum_list(N, num_list):
    # 누적합 리스트
    sum_list = [0 for _ in range(N+1)]

    i = 1
    while True:
        # 종료 조건
        if i == N+1:
            return sum_list
        
        # 이전까지의 누적합에 현재 수 합하기
        sum_list[i] = sum_list[i-1] + num_list[i]
        i += 1


N, M = map(int, input().split())
num_list = [0] + list(map(int, input().split()))
data_list = [list(map(int, input().split())) for _ in range(M)]
solution(N, M, num_list, data_list)