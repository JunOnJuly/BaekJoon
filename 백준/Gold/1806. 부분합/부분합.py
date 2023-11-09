def solution(N, S, data_list):
    # 누적합 리스트
    stack_sum = [0] + data_list
    for idx in range(1, len(stack_sum)):
        stack_sum[idx] += stack_sum[idx-1]
    # 투포인터
    start = 0
    end = 1
    # 최소길이
    min_length = 1000001
    while True:
        # end 가 인덱스를 벗어나면 끝
        if end > N:
            # 값을 만들 수 없으면
            if min_length == 1000001:
                return 0
            else:
                return min_length
        # 포인터에 해당하는 값
        start_value = stack_sum[start]
        end_value = stack_sum[end]
        # 부분 합
        sub = end_value - start_value
        # 부분 합이 S 이상이면
        if sub >= S:
            # 최소길이 최신화
            # start 와 end 가 같으면 패스
            if start != end and min_length > end-start:
                min_length = end-start
            # start 포인터 + 1
            start += 1
        # 부분 합이 S 이하면
        else:
            # end 포인터 + 1
            end += 1


N, S = map(int, input().split())
data_list = list(map(int, input().split()))
print(solution(N, S, data_list))