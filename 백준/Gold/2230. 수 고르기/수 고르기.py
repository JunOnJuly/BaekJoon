def solution(N, M, data_list):
    # 정렬
    data_list = sorted(data_list)
    # 차이의 최솟값
    min_sub = 2000000000
    # 투포인터
    left = 0
    right = 1
    while True:
        # right 가 범위를 벗어나면
        if right >= N:
            return min_sub
        # 포인터에 해당하는 값
        left_value = data_list[left]
        right_value = data_list[right]
        # 차이
        sub = right_value - left_value
        # 차이가 M이면
        if sub == M:
            return M
        # 차이가 M보다 크면
        elif sub > M:
            # 최솟값 최신화
            if min_sub > sub:
                min_sub = sub
            # 왼쪽 포인터 + 1
            left += 1
            continue
        # 차이가 M보다 작으면
        else:
            # 오른쪽 포인터 + 1
            right += 1
            continue


N, M = map(int, input().split())
data_list = [int(input()) for _ in range(N)]
print(solution(N, M, data_list))