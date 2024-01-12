def solution(N, data_list):
    # 남은 사과 합
    left_sum = 0
    # 데이터 순회
    for std_num, app_num in data_list:
        # 나머지 합
        left_sum += app_num%std_num
    print(left_sum)


N = int(input())
data_list = [list(map(int, input().split())) for _ in range(N)]
solution(N, data_list)